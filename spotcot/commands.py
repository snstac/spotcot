#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Spot Cursor-on-Target Gateway Commands."""

import asyncio
import argparse
import collections
import concurrent
import configparser
import logging
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
    cot_url: urllib.parse.ParseResult = urllib.parse.urlparse(opts.get("COT_URL"))

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

    parser.add_argument("-c", "--CONFIG_FILE", dest="CONFIG_FILE", default="config.ini", type=str)
    parser.add_argument(
        "-d", "--DEBUG", dest="DEBUG", default=False, action="store_true", help="Enable DEBUG logging")
    parser.add_argument(
        '-U',
        '--COT_URL',
        dest="COT_URL",
        help='URL to CoT Destination. Must be a URL, e.g. tcp:1.2.3.4:1234 or tls:...:1234, etc.'
    )
    parser.add_argument(
        '-S',
        '--COT_STALE',
        dest="COT_STALE",
        help='CoT Stale period, in seconds',
        default=spotcot.DEFAULT_COT_STALE
    )
    parser.add_argument(
        '-k', '--API_KEY', help='Spot API Key ("XML Feed Id").',
    )
    parser.add_argument(
        '-i',
        '--POLL_INTERVAL',
        dest="POLL_INTERVAL",
        help='Spot API Polling Interval.',
        default=spotcot.DEFAULT_POLL_INTERVAL
    )
    parser.add_argument(
        '-P',
        '--SPOT_PASSWORD',
        dest="SPOT_PASSWORD",
        help='[Optional] Spot API Password for Private Feeds.'
    )
    namespace = parser.parse_args()
    cli_args = {k: v for k, v in vars(namespace).items() if v is not None}

    # Read config file:
    config_file = cli_args.get("CONFIG_FILE")
    logging.info("Reading configuration from %s", config_file)
    config = configparser.ConfigParser()
    config.read(config_file)

    # Combined command-line args with config file:
    if "spotcot" in config:
        combined_config = collections.ChainMap(cli_args, os.environ, config["spotcot"])
    else:
        combined_config = collections.ChainMap(cli_args, os.environ)

    if not combined_config.get("COT_URL"):
        print("Please specify a CoT Destination URL, for example: '-U tcp:takserver.example.com:8087'")
        print("See -h for help.")
        sys.exit(1)

    if not combined_config.get("API_KEY"):
        print('Please specify a Spot API Key ("XML Feed Id")., for example: "-k 1234abc"')
        print("See -h for help.")
        sys.exit(1)

    if sys.version_info[:2] >= (3, 7):
        asyncio.run(main(combined_config), debug=combined_config.get("DEBUG"))
    else:
        loop = get_event_loop()
        try:
            loop.run_until_complete(main(combined_config))
        finally:
            loop.close()


if __name__ == '__main__':
    cli()
