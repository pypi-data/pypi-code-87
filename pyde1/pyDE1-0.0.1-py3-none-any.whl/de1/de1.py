"""
Copyright © 2021 Jeff Kletsky. All Rights Reserved.

License for this software, part of the pyDE1 package, is granted under
GNU General Public License v3.0 only
SPDX-License-Identifier: GPL-3.0-only
"""

import asyncio
import atexit
import logging
import struct
import time

from copy import copy
from typing import Union, Dict, Coroutine, Optional, List

from bleak import BleakClient
from bleak.backends.device import BLEDevice
from bleak.backends.scanner import AdvertisementData

import pyDE1.default_logger

from pyDE1.de1.exceptions import DE1NoAddressError, DE1NoHandlerError, \
    DE1ValueError
from pyDE1.de1.ble import UnsupportedBLEActionError

# general utilities

from pyDE1.de1.c_api import \
    PackedAttr, RequestedState, ReadFromMMR, WriteToMMR, StateInfo, \
    FWMapRequest, FWErrorMapRequest, FWErrorMapResponse, \
    API_MachineStates, API_Substates, MAX_FRAMES, get_cuuid, MMR0x80LowAddr, \
    packed_attr_from_cuuid, pack_one_mmr0x80_write, DE1APIValueError

from pyDE1.de1.ble import CUUID
from pyDE1.de1.notifications import NotificationState, MMR0x80Data
from pyDE1.de1.profile import ProfileByFrames, DE1ProfileValidationError

from pyDE1.i_target_manager import I_TargetManager

# Importing from the module-level init fails
# from pyDE1.flow_sequencer import I_TargetManager

from pyDE1.de1.firmware_file import FirmwareFile

import pyDE1.de1.handlers

from pyDE1.event_manager import SubscribedEvent
from pyDE1.de1.events import ShotSampleUpdate, \
    ShotSampleWithVolumesUpdate

# If True, randomly skips upload packets
_TEST_BLE_LOSS_DURING_FW_UPLOAD = False
if _TEST_BLE_LOSS_DURING_FW_UPLOAD:
    import random

logger = logging.getLogger('de1')

# TODO: Initialization should be able to be done by address or BLEDevice
#       NB: https://github.com/hbldh/bleak/issues/361 on Linux and scan

# TODO: Scanner that can return first quickly or all within a time period

# NB: It doesn't look like CoreBluetooth reveals an identifier that is stable
#     across boots.  It uses a UUID rather than the MAC address of the device.

class DE1:

    def __init__(self, address=None):
        self._address = address
        self._name = None
        self._bleak_client: Optional[BleakClient] = None
        self._flow_sequencer: Optional[I_TargetManager] = None

        # TODO: Should the handlers be able to be changed on the fly?
        self._handlers = pyDE1.de1.handlers.default_handler_map(self)

        # The _cuuid_dict and _mmr_dict dictionaries contain the last update
        # TODO: Where is "last heard from"?
        self._cuuid_dict: Dict[CUUID, NotificationState] = dict()
        self._mmr_dict: Dict[Union[MMR0x80LowAddr, int], MMR0x80Data] = dict()
        for cuuid in CUUID:
            self._cuuid_dict[cuuid] = NotificationState(cuuid)
        for mmr in MMR0x80LowAddr:
            self._mmr_dict[mmr] = MMR0x80Data(mmr)

        self._event_state_update = SubscribedEvent(self)
        self._event_shot_sample = SubscribedEvent(self)
        self._event_water_levels = SubscribedEvent(self)
        self._event_shot_sample_with_volumes_update = SubscribedEvent(self)

        # These have to be valid, as may be tested before first update
        self._cuuid_dict[CUUID.StateInfo]._last_value = StateInfo(
            State=API_MachineStates.NoRequest,
            SubState=API_Substates.NoState
        )

        # Used to restrict multiple access to writing the active profile
        self._profile_lock = asyncio.Lock()

        self._line_frequency = 60  # Hz TODO: Estimate or read this

        self._tracking_volume_dispensed = False
        self._volume_dispensed_total = 0
        self._volume_dispensed_preinfuse = 0
        self._volume_dispensed_pour = 0
        self._volume_dispensed_by_frame = []
        # TODO: Convince Ray to return substate and state
        #       in ShotSample so this isn't needed for volume tracking
        self._number_of_preinfuse_frames: int = 0

        self._last_stop_requested = 0

        # Internal flag
        self._recorder_active = False

        # Used for volume estimation at this time
        asyncio.create_task(self._event_shot_sample.subscribe(
            self._create_self_callback_ssu()))


    @classmethod
    def device_adv_is_recognized_by(cls, device: BLEDevice, adv: AdvertisementData):
        return adv.local_name == "DE1"

    @property
    def stop_lead_time(self):
        return 0.1  # seconds, TODO: Where does this belong?

    @property
    def address(self):
        return self._address

    @property
    def name(self):
        return self._name

    @property
    def event_state_update(self):
        return self._event_state_update

    @property
    def event_shot_sample(self):
        return self._event_shot_sample

    @property
    def event_water_levels(self):
        return self._event_water_levels

    @property
    def event_shot_sample_with_volumes_update(self):
        return self._event_shot_sample_with_volumes_update

    # NB: Linux apparently "needs" a scan when connecting by address
    #     It may be the case that this disconnects other devices
    #     See: https://github.com/hbldh/bleak/issues/361

    async def connect(self, timeout=5.0):
        logger.info(f"Connecting to DE1 at {self.address}")
        if self._bleak_client is None:
            if self.address is None:
                raise DE1NoAddressError
            self._bleak_client = BleakClient(self.address)
        await self._bleak_client.connect(timeout=timeout)
        if self.is_connected:
            logger.info(f"Connected to DE1 at {self.address}")
            self.register_atexit_disconnect()
        else:
            logger.error(f"Connection failed to DE1 at {self.address}")

    async def disconnect(self):
        logger.info(f"Disconnecting from DE1")
        if self._bleak_client is None:
            logger.info(f"Disconnecting from DE1; no client")
        await self._bleak_client.disconnect()
        if self.is_connected:
            logger.error(f"Disconnect failed from DE1 at {self.address}")
        else:
            logger.info(f"Disconnected from DE1 at {self.address}")
        # TODO: Unregister atexit disconnect

    def _atexit_disconnect(self):
        """
        Try a closure to capture self
        """
        def sync_disconnect():
            nonlocal self
            if not self.is_connected:
                logger.debug("atexit sync_disconnect: Not connected to DE1")
                return
            else:
                logger.info(f"atexit sync_disconnect: Disconnecting DE1")
                loop = asyncio.get_event_loop()
                loop.run_until_complete(self.disconnect())
        return sync_disconnect

    def register_atexit_disconnect(self):
        atexit.register(self._atexit_disconnect())


    # TODO: Decide how to handle  self._disconnected_callback

    @property
    def is_connected(self):
        if self._bleak_client is None:
            return False
        else:
            return self._bleak_client.is_connected

    async def start_notifying(self, cuuid: CUUID):
        try:
            done = self._cuuid_dict[cuuid].mark_requested()
            await self._bleak_client.start_notify(cuuid.uuid,
                                                  self._handlers[cuuid])
            logging.getLogger(cuuid.__str__()).debug("Start notify")
        except KeyError:
            raise DE1NoHandlerError(f"No handler found for {cuuid}")
        return done

    async def stop_notifying(self, cuuid: CUUID):
        try:
            done = self._cuuid_dict[cuuid].mark_ended()
            await self._bleak_client.stop_notify(cuuid.uuid)
            logging.getLogger(cuuid.__str__()).debug("Stop notify")
        except KeyError:
            raise DE1NoHandlerError(f"No handler found for {cuuid}")
        return done

    async def start_standard_notifiers(self):
        """
        Enable the return of read requests from MMR
        as well as the current, periodic reports:
        ShotSample, StateInfo, and WaterLevels
        """
        await self.start_notifying(CUUID.ReadFromMMR)
        await self.start_notifying(CUUID.ShotSample)
        await self.start_notifying(CUUID.StateInfo)
        await self.start_notifying(CUUID.WaterLevels)

    async def read_cuuid(self, cuuid: CUUID):
        logging.getLogger(f"{cuuid.__str__()}.Read").debug("Requested")
        wire_bytes = await self._bleak_client.read_gatt_char(cuuid.uuid)
        obj = packed_attr_from_cuuid(cuuid, wire_bytes)
        self._cuuid_dict[cuuid].mark_updated(obj)
        return obj

    async def write_packed_attr(self, obj: PackedAttr):
        cuuid = get_cuuid(obj)
        logging.getLogger(f"{cuuid.__str__()}.Write").debug(obj.log_string())
        return await self._bleak_client.write_gatt_char(cuuid.uuid,
                                                        obj.as_wire_bytes())

    async def write_packed_attr_return_notification(self, obj: PackedAttr):
        """
        Write to the CUUID, then wait for the first response

        This is unsafe right now if not notifying already
        or if on a CUUID that doesn't notify after a write
        either in general, or due to an unrecognized command.

        This also isn't robust to overlapping requests

        TODO: Consider how to handle multi-packet requests (MMR)
              and what "done" means in that case
        """
        cuuid = get_cuuid(obj)
        logger = logging.getLogger(cuuid.__str__())
        if not cuuid.can_write_then_return():
            raise UnsupportedBLEActionError(
                "write_cuuid_return_notification not supported for " \
                + cuuid.__str__()
            )
        logger.debug(f"Acquiring write/return lock")
        async with cuuid.lock:
            logger.debug(f"Acquired write/return lock")
            # TODO: This order should work, though potential race condition
            notification_state = self._cuuid_dict[cuuid]
            await self.write_packed_attr(obj)
            notification_state.mark_requested()
            logger.debug(f"Waiting for notification")
            await notification_state.ready_event.wait()
            logger.debug(f"Returning notification")
            return notification_state.last_value

    async def _request_state(self, State: API_MachineStates):
        rs = RequestedState(State)
        await self.write_packed_attr(rs)

    # TODO: Should this be public or private?
    async def read_mmr(self, length, addr_high, addr_low, data=b''
                       ) -> List[asyncio.Event]:
        mmr = ReadFromMMR(Len=length, addr_high=addr_high, addr_low=addr_low,
                          Data=data)
        packed = mmr.as_wire_bytes()
        ready_events = list()
        if addr_high == 0x80:
            #
            # TODO: Revisit this
            #
            # The stride of MMR0x80Data is going to be 4 bytes except
            # in the debug log region, where it will be 16 bytes
            #
            # There is the possibility of moving from one region to another
            # that is not accounted for here
            #
            if mmr.is_within_debug_log:
                stride = 16
            else:
                stride = 4
            request_time = time.time()
            for addr in range(addr_low, (addr_low + (mmr.Len + 1) * 4), stride):
                if addr not in self._mmr_dict:
                    self._mmr_dict[addr] = MMR0x80Data(addr)
                ready_events.append(
                    self._mmr_dict[addr].mark_requested(request_time)
                )
        await self.write_packed_attr(mmr)
        return ready_events

    async def read_one_mmr0x80(self, mmr0x80: MMR0x80LowAddr) -> asyncio.Event:
        ready_events = await self.read_mmr(
            length=4,
            addr_high=0x80,
            addr_low=mmr0x80
        )
        return ready_events[0]

#
# MMR-based properties
#

    async def read_standard_mmr_registers(self):
        """
        Request a read of the readable MMR registers, in bulk
        :return:
        """
        start_block_1 = MMR0x80LowAddr.HW_CONFIG
        end_block_1 = MMR0x80LowAddr.FIRMWARE_BUILD_NUMBER
        words_block_1 = int((end_block_1 - start_block_1) / 4)

        start_block_2 = MMR0x80LowAddr.FAN_THRESHOLD
        end_block_2 = MMR0x80LowAddr.GHC_INFO
        words_block_2 = int((end_block_2 - start_block_2) / 4)

        start_block_3 = MMR0x80LowAddr.STEAM_FLOW_RATE
        end_block_3 = MMR0x80LowAddr.FLOW_CALIBRATION
        words_block_3 = int((end_block_3 - start_block_3) / 4)

        # Generated "bleak.exc.BleakDBusError: org.bluez.Error.InProgress"
        # from assert_reply in write_gatt_char in block_3 write
        #
        # Not clear if this is by adapter, device, or characteristic
        #
        # await asyncio.gather(
        #     self.read_mmr(words_block_1 - 1, 0x80, start_block_1),
        #     self.read_mmr(words_block_2 - 1, 0x80, start_block_2),
        #     self.read_mmr(words_block_3 - 1, 0x80, start_block_3),
        # )

        await self.read_mmr(words_block_1, 0x80, start_block_1)
        await self.read_mmr(words_block_2, 0x80, start_block_2)
        await self.read_mmr(words_block_3, 0x80, start_block_3)

    #
    # Upload a shot profile
    #

    async def upload_profile(self, profile: ProfileByFrames,
                             override_flow_sequencer_targets=True):

        # TODO: How does this get interrupted if an API call requests
        #       a different profile to be uploaded?

        if not profile.validate():
            raise DE1ProfileValidationError

        for cuuid in (CUUID.HeaderWrite, CUUID.FrameWrite):
            if not self._cuuid_dict[cuuid].is_notifying:
                done = await self.start_notifying(cuuid)
                # await done.wait()

        if profile.number_of_preinfuse_frames is not None:
            self._number_of_preinfuse_frames = \
                profile.number_of_preinfuse_frames

        if profile.tank_temperature is not None:
            await self.write_and_read_back_mmr0x80(
                addr_low=MMR0x80LowAddr.TANK_WATER_THRESHOLD,
                value=profile.tank_temperature
            )

        if override_flow_sequencer_targets and self._flow_sequencer is not None:

            if (target := profile.target_volume) is not None:
                if target <= 0:
                    target = None
                self._flow_sequencer.stop_at_volume_set(
                    state=API_MachineStates.Espresso,
                    volume=target
                )

            if (target := profile.target_weight) is not None:
                if target <= 0:
                    target = None
                self._flow_sequencer.stop_at_weight_set(
                    state=API_MachineStates.Espresso,
                    weight=target
                )

        # async with asyncio.wait_for(self._profile_lock.acquire(), timeout=3):
        async with self._profile_lock:

            # TODO: Should there be some way to acquire lock on the two CUUIDs?

            await self.write_packed_attr(profile.header_write())
            for frame in profile.shot_frame_writes():
                await self.write_packed_attr(frame)
            for frame in profile.ext_shot_frame_writes():
                await self.write_packed_attr(frame)
            await self.write_packed_attr(profile.shot_tail_write())

    async def write_and_read_back_mmr0x80(self, addr_low: MMR0x80LowAddr,
                                          value: float):

        if not addr_low.writable:
            raise DE1APIValueError(
                f"MMR target address not writable: {addr_low.__repr__()}")
        if not addr_low.readable:
            raise DE1APIValueError(
                f"MMR target address not readable: {addr_low.__repr__()}")

        mmr_record = self._mmr_dict[addr_low]

        if mmr_record.last_requested is None:
            await self.read_one_mmr0x80(addr_low)
        if not mmr_record.ready_event.is_set():
            logger.info(f"About to wait for {addr_low.__repr__()}")
        await mmr_record.ready_event.wait()

        # old = mmr_record.data_decoded
        # value = (old + 0.1) % 20
        # logger.info(f"old and new t: {old} {value}")

        if value != mmr_record.data_decoded:
            pa = pack_one_mmr0x80_write(addr_low,
                                        value)
            await self.write_packed_attr(pa)

            # Queue a read-back to update DE1
            asyncio.create_task(
                self.read_one_mmr0x80(addr_low))

    #
    # Firmware updating
    #

    # TODO: Does it need a lock?

    async def upload_firmware(self, fw: FirmwareFile):
        start_addr = 0x000000
        write_size = 0x10
        offsets = range(0, len(fw.file_contents), write_size)

        await self._request_state(API_MachineStates.Sleep)
        await self.start_notifying(CUUID.FWMapRequest)

        fw_map_result = await self.write_packed_attr_return_notification(
            FWMapRequest(
                WindowIncrement=0,
                FWToErase=1,
                FWToMap=1,
                FirstError=FWErrorMapRequest.Ignore
            )

        )

        # Intentionally "fail" the upload

        for offset in offsets[0:10]:
            if _TEST_BLE_LOSS_DURING_FW_UPLOAD \
                    and random.choices((True, False), cum_weights=(0.001, 1))[0]:
                logger.info(f"Randomly skipping 0x{offset:06x}")
                continue
            data = fw.file_contents[offset:(offset + write_size)]
            await self.write_packed_attr(
                WriteToMMR(
                    Len=len(data),
                    Address=(start_addr + offset),
                    Data=data,
                )
            )

        # TODO: Is there something better here?
        await asyncio.sleep(1)

        fw_map_result = await self.write_packed_attr_return_notification(
            FWMapRequest(
                WindowIncrement=0,
                FWToErase=0,
                FWToMap=1,
                FirstError=FWErrorMapRequest.ReportFirst
            )
        )

        success =  fw_map_result.FirstError == FWErrorMapResponse.NoneFound
        if not success:
            logger.error(
                "Error(s) in firmware upload. "
                f"First at 0x{fw_map_result.FirstError:06x}"
            )

        return success

        #
        # I couldn't get this to work, always getting "stuck" on the first addr
        # even when patching with a single-packet upload.
        # Leaving it here for reference -- 2021-05-25
        #

        #
        # Fill in any gaps
        #

        # count_limit = 10
        # count = 0
        # retval = False
        #
        # done = fw_map_result.FirstError == FWErrorMapResponse.NoneFound
        #
        # while not done:
        #     fw_map_result = await self.write_cuuid_return_notification(
        #         CUUID.FWMapRequest, FWMapRequest(
        #             WindowIncrement=0,
        #             FWToErase=0,
        #             FWToMap=1,
        #             FirstError=FWErrorMapRequest.ReportNext
        #         )
        #     )
        #     count += 1
        #     done = (fw_map_result.FirstError == FWErrorMapResponse.NoneFound
        #             or count > count_limit)
        #
        # while count < count_limit:
        #     fw_map_result = await self.write_cuuid_return_notification(
        #         CUUID.FWMapRequest, FWMapRequest(
        #             WindowIncrement=0,
        #             FWToErase=0,
        #             FWToMap=1,
        #             FirstError=FWErrorMapRequest.ReportFirst
        #         )
        #     )
        #     logger.debug(f"Report first: {fw_map_result.log_string()}")
        #     fix_addr = fw_map_result.FirstError
        #     if fix_addr == FWErrorMapResponse.NoneFound:
        #         retval = True
        #         break
        #     while count < count_limit:
        #         count += 1
        #         offset = fix_addr - start_addr
        #         data = fw.file_contents[offset:(offset + write_size)]
        #         await self.write_cuuid(
        #             CUUID.WriteToMMR, WriteToMMR(
        #                 Len=len(data),
        #                 Address=(start_addr + offset),
        #                 Data=data,
        #             )
        #         )
        #         fw_map_result = await self.write_cuuid_return_notification(
        #             CUUID.FWMapRequest, FWMapRequest(
        #                 WindowIncrement=0,
        #                 FWToErase=0,
        #                 FWToMap=1,
        #                 FirstError=FWErrorMapRequest.ReportNext
        #             )
        #         )
        #         logger.debug(f"Report next: {fw_map_result.log_string()}")
        #         fix_addr = fw_map_result.FirstError
        #         if fix_addr == FWErrorMapResponse.NoneFound:
        #             break
        #
        # return retval

    @property
    def current_state(self) -> API_MachineStates:
        return self._cuuid_dict[CUUID.StateInfo].last_value.State

    @property
    def current_substate(self) -> API_Substates:
        return self._cuuid_dict[CUUID.StateInfo].last_value.SubState

    # Perhaps one day line frequency will be reported by the firmware
    # Needed for volume estimation

    @property
    def line_frequency(self) -> int:
        return self._line_frequency

    @line_frequency.setter
    def line_frequency(self, value):
        if value not in [50, 60]:
            raise DE1ValueError(f"Line frequency must be 50 or 60 ({value})")

    # Perhaps one day volume dispensed will be tracked by the firmware

    @property
    def volume_dispensed_preinfuse(self):
        return self._volume_dispensed_preinfuse

    @property
    def volume_dispensed_pour(self):
        return self._volume_dispensed_pour

    @property
    def volume_dispensed_total(self):
        return self._volume_dispensed_total

    @property
    def volume_dispensed_by_frame(self):
        """
        A list of estimated volume dispensed by frame
        """
        return copy(self._volume_dispensed_by_frame)

    def _reset_volume_dispensed(self):
        self._volume_dispensed_preinfuse = 0
        self._volume_dispensed_pour = 0
        self._volume_dispensed_total = 0
        self._volume_dispensed_by_frame = [0] * MAX_FRAMES

    def _create_self_callback_ssu(self) -> Coroutine:
        de1 = self
        last_sample_time = 0
        start_up = True

        async def de1_self_callback(ssu: ShotSampleUpdate):
            nonlocal de1, last_sample_time, start_up

            # Track volume dispensed

            # TODO: Reconstruct original DE1 clock prior to EventPayload

            # sample time is counts of half-cycles in a 16-bit unsigned int
            # Expect 25 if nothing is missed, 4 per second on 50 Hz, ~5 on 60
            if start_up:
                start_up = False
            else:
                t_inc = ssu.sample_time - last_sample_time
                if t_inc < 0:
                    t_inc += 65536
                use_this = False
                if 24 < t_inc < 26:
                    use_this = True
                elif 49 < t_inc < 51:
                    use_this = True
                    logger.warning(
                        f"Skipped update at {t_inc} samples? {ssu}"
                    )
                else:
                    use_this = False
                    # Changed to warning (from error) here as seems to happen
                    # around state change reports and heavy BLE traffic
                    logger.warning(
                        f"Unexpected update period {t_inc} from {ssu}"
                    )

                if use_this and de1._tracking_volume_dispensed:
                    v_inc = ssu.group_flow * t_inc / (de1.line_frequency * 2)
                    # since de1.volume_dispensed creates a copy,
                    # and this should be the only "writer" other than clear
                    # don't use a lock

                    # TODO: Convince Ray to return substate and state
                    #       in ShotSample so don't need to use frame count
                    if ssu.frame_number > de1._number_of_preinfuse_frames:
                        de1._volume_dispensed_pour += v_inc
                    else:
                        de1._volume_dispensed_preinfuse += v_inc
                    de1._volume_dispensed_total += v_inc
                    de1._volume_dispensed_by_frame[ssu.frame_number] += v_inc

            last_sample_time = ssu.sample_time

            await de1._event_shot_sample_with_volumes_update.publish(
                ShotSampleWithVolumesUpdate(
                    ssu,
                    volume_preinfuse=self._volume_dispensed_preinfuse,
                    volume_pour=self._volume_dispensed_pour,
                    volume_total=self._volume_dispensed_total,
                    volume_by_frame=self._volume_dispensed_by_frame,
                )
            )

        return de1_self_callback

    async def skip_to_next(self):
        """
        Requests the next frame if in Espresso mode.

        Tries to go to Idle in other modes
        """
        was_espresso = self.current_state == API_MachineStates.Espresso
        await self._request_state(API_MachineStates.SkipToNext)
        if was_espresso:
            logger.info("Skip to next request made")
        else:
            logger.warning(
                "Skip to next request granted while in "
                f"{self.current_state.name}")

    async def stop_flow(self):
        """
        If in a flow state, request stopping flow
        Replaces legacy "go to Idle"
        """
        # TODO Can the logic around "already asked, wait a bit" be cleaned up?
        logger.info("stop_flow() called")
        reasonable_stop_time = 0.25  # seconds after request
        if self.current_state.is_flow_state \
                and self.current_substate.flow_phase in ['before', 'during'] \
                and (now := time.time() - self._last_stop_requested) \
                    > reasonable_stop_time:
            self._last_stop_requested = now
            await self._request_state(API_MachineStates.Idle)

    async def idle(self):
        """
        This is an explicit request for Idle.

        de1.stop_flow() is probably more appropriate in many cases
        """
        logger.info("idle() called")
        await self._request_state(API_MachineStates.Idle)

    async def sleep(self):
        logger.info("sleep() called")
        if self.current_state not in (API_MachineStates.Idle,
                                      API_MachineStates.GoingToSleep):
            logger.warning(
                "Sleep requested while in {}, {}. Calling idle() first.".format(
                    self.current_state.name, self.current_substate.name
                ))
            await self.idle()
            # TODO: Really should wait here until Idle seen
            #       If so, how to deal with it if it doesn't idle soon?
        await self._request_state(API_MachineStates.Sleep)

    # TODO: Support for starting the four modes for non-GHC machines

    # TODO: Support for clean, descale, travel

    # TODO: Settings object that then uploads if needed