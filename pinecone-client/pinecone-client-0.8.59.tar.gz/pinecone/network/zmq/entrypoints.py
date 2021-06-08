#
# Copyright (c) 2020-2021 Pinecone Systems Inc. All right reserved.
#

from pinecone.protos import core_pb2
from pinecone.utils.exceptions import RestartException
from pinecone.network.zmq.spec import ServletSpec
from pinecone.network.zmq.servlet import ZMQServlet
from pinecone.utils.constants import RECV_TIMEOUT
from pinecone.network.zmq.wal import WALServlet

from loguru import logger
import asyncio
from typing import Awaitable, Callable, List


def start(servlet_spec: ServletSpec, volume_request=None, persistent_dir=None, num_replicas=None, sync_msg_handler=None,
          stats_exporter=None):
    logger.info('starting zmq servlet: %s ' % servlet_spec.function_name)

    try:
        loop = asyncio.get_event_loop()
        if loop.is_closed():
            raise RuntimeError()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    if volume_request:
        servlet = WALServlet(servlet_spec, persistent_dir, volume_request=volume_request)
        servlet.start_polling()
        logger.info(f"Before reload: {servlet_spec.get_stats()}")
        loop.run_until_complete(servlet.run_sync(servlet.load_sync, sync_msg_handler))
        logger.info(f"After reload: {servlet_spec.get_stats()}")
    else:
        servlet = ZMQServlet(servlet_spec)
        servlet.start_polling()

    if stats_exporter:
        loop.create_task(stats_exporter())

    servlet.start_reload_task()
    loop.set_exception_handler(servlet.handle_exception)
    loop.run_forever()
    loop.close()
    if servlet.exception is not None and type(servlet.exception) == RestartException:
        logger.error('Restarting...')


def run_in_servlet(servlet_spec: ServletSpec, function: Callable[..., Awaitable], *args):
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    servlet = ZMQServlet(servlet_spec)
    result = asyncio.run(function(servlet, *args))
    loop.stop()
    return result


def run_in_wal_servlet(servlet_spec: ServletSpec, persistent_dir: str, function: Callable[..., Awaitable], *args):
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    servlet = WALServlet(servlet_spec, persistent_dir)
    result = asyncio.run(function(servlet, *args))
    servlet.cleanup()
    loop.stop()
    return result


async def recv_requests(servlet: ZMQServlet, num: int):
    msgs = []
    while len(msgs) < num:
        try:
            msgs.append(await asyncio.wait_for(servlet.recv_msg(servlet.zmq_ins[num]), RECV_TIMEOUT))
            logger.success(msgs[-1])
        except asyncio.TimeoutError:
            logger.error('timed out')
            continue
    return msgs


async def recv_logs(servlet: WALServlet, num: int):
    msgs = []
    while len(msgs) < num:
        try:
            msg = await asyncio.wait_for(servlet.recv_log_msg(), RECV_TIMEOUT)
            await servlet.handle_log_msg(msg)
            msgs.append(msg)
        except asyncio.TimeoutError:
            continue
    return msgs


async def send_replay_request(servlet: WALServlet, offset: int, total_num: int):
    await servlet.send_log_msg(servlet.get_replay_request(override_offset=offset), 0)
    await recv_logs(servlet, total_num)


async def send_logs(servlet: WALServlet, log: List['core_pb2.LogEntry'], replica: int):
    for msg in log:
        await servlet.send_log_msg(msg, replica)


async def send_requests(servlet: ZMQServlet, requests: List['core_pb2.Request']):
    for msg in requests:
        await servlet.send_msg(msg)
