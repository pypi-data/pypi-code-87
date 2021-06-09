"""
Copyright © 2021 Jeff Kletsky. All Rights Reserved.

License for this software, part of the pyDE1 package, is granted under
GNU General Public License v3.0 only
SPDX-License-Identifier: GPL-3.0-only


Utilities to be able to write a "shot file" containing the digested data
that describe how the shot progressed
"""
import logging
import time

from typing import Optional, Coroutine

import pyDE1.default_logger

from pyDE1.de1.c_api import API_MachineStates
from pyDE1.event_manager import SubscribedEvent
from pyDE1.de1.events import ShotSampleUpdate, ShotSampleWithVolumesUpdate
from pyDE1.scale.events import WeightAndFlowUpdate

# logger = logging.getLogger('ShotFile')

import aiologger
logger = aiologger.Logger.with_default_handlers()



async def basic_shot_sample_logger(ssu: ShotSampleWithVolumesUpdate):
    now = time.time()
    line = "{:5.2f} {:5.2f} {:6.1f} {:2d}     {:5d}  {:0.3f} {:0.3f} ms".format(
        ssu.group_pressure,
        ssu.group_flow,
        ssu.mix_temp,
        ssu.frame_number,
        ssu.sample_time,
        (ssu.create_time - ssu.arrival_time) * 1000,
        (now - ssu.arrival_time) * 1000,
    )
    logger.info(line)


async def gated_basic_shot_sample_logger(sswvu: ShotSampleWithVolumesUpdate):
    now = time.time()
    if sswvu.sender._recorder_active:
        line = "{:5.2f} {:5.2f} {:4.1f} {:2d} {:.1f} {:.1f} {:.1f} {} " \
                "{:5d}  {:0.3f} {:0.3f} ms".format(
            sswvu.group_pressure,
            sswvu.group_flow,
            sswvu.mix_temp,
            sswvu.frame_number,
            sswvu.volume_preinfuse,
            sswvu.volume_pour,
            sswvu.volume_total,
            [round(v,1) for v in sswvu.volume_by_frames],
            sswvu.sample_time,
            (sswvu.create_time - sswvu.arrival_time) * 1000,
            (now - sswvu.arrival_time) * 1000,
        )
        logger.info(line)


class CombinedShotLogger:

    def __init__(self):
        self._last_weight = 0
        self._last_flow = 0

    async def sswvu_subscriber(self, sswvu: ShotSampleWithVolumesUpdate):
        now = time.time()
        if sswvu.sender._recorder_active:
            line = "{:5.2f} b  {:4.2f} mL/s  {:4.2f} g/s  {:5.1f} g  " \
                   "{:4.1f} °C " \
                   "{:2d} {:.1f} {:.1f} {:.1f} {} " \
                   "{:5d}  {:0.3f} {:0.3f} ms".format(
                sswvu.group_pressure,
                sswvu.group_flow,
                self._last_flow,
                self._last_weight,
                sswvu.mix_temp,
                sswvu.frame_number,
                sswvu.volume_preinfuse,
                sswvu.volume_pour,
                sswvu.volume_total,
                [round(v, 1) for v in sswvu.volume_by_frames],
                sswvu.sample_time,
                (sswvu.create_time - sswvu.arrival_time) * 1000,
                (now - sswvu.arrival_time) * 1000,
            )
            logger.info(line)

    async def wafu_subscriber(self, wafu: WeightAndFlowUpdate):
        self._last_flow = wafu.average_flow
        self._last_weight = wafu.current_weight