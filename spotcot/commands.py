#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Spot Cursor-on-Target Gateway Commands."""

import asyncio
import argparse
import collections
import concurrent
import configparser
import os
import sys
import time
import urllib

import pytak

import spotcot

# Python 3.6 support:
if sys.version_info[:2] >= (3, 7):
    from asyncio import get_running_loop
else:
    from asyncio import _get_running_loop as get_running_loop


__author__ = "Greg Albrecht W2GMD <oss@undef.net>"
__copyright__ = "Copyright 2021 Orion Labs, Inc."
__license__ = "Apache License, Version 2.0"


async def main(opts):
    loop = get_running_loop()
    tx_queue: asyncio.Queue = asyncio.Queue()
    rx_queue: asyncio.Queue = asyncio.Queue()
    cot_url: urllib.parse.ParseResult = urllib.parse.urlparse(opts.cot_url)

    # Create our CoT Event Queue Worker
    reader, writer = await pytak.protocol_factory(cot_url)
    write_worker = pytak.EventTransmitter(tx_queue, writer)
    read_worker = pytak.EventReceiver(rx_queue, reader)

    message_worker = spotcot.SpotWorker(tx_queue, opts)

    await tx_queue.put(pytak.hello_event("spotcot"))

    done, pending = await asyncio.wait(
        set([message_worker.run(), read_worker.run(), write_worker.run()]),
        return_when=asyncio.FIRST_COMPLETED)

    for task in done:
        print(f"Task completed: {task}")


def cli():
    """Command Line interface for Spot Cursor-on-Target Gateway."""

    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-U', '--cot_url', help='URL to CoT Destination.',
        required=True
    )
    parser.add_argument(
        '-S', '--cot_stale', help='CoT Stale period, in seconds',
    )

    parser.add_argument(
        '-k', '--api_key', help='Spot API Key ("XML Feed Id").', required=True
    )
    parser.add_argument(
        '-i', '--interval', help='Spot API Query Interval.', default=600
    )
    parser.add_argument(
        '-p', '--password', help='Spot Feed Password for private feeds.'
    )

    opts = parser.parse_args()

    if sys.version_info[:2] >= (3, 7):
        asyncio.run(main(opts), debug=bool(os.getenv("DEBUG")))
    else:
        loop = get_event_loop()
        try:
            loop.run_until_complete(main(opts))
        finally:
            loop.close()


if __name__ == '__main__':
    cli()
