#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Spot Cursor-on-Target Gateway Commands."""

import argparse
import time

import spotcot

__author__ = 'Greg Albrecht W2GMD <oss@undef.net>'
__copyright__ = 'Copyright 2020 Orion Labs, Inc.'
__license__ = 'Apache License, Version 2.0'


def cli():
    """Command Line interface for Spot Cursor-on-Target Gateway."""

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-k', '--api_key', help='Spot API Key ("XML Feed Id")', required=True
    )
    parser.add_argument(
        '-i', '--interval', help='Spot API Query Interval', default=600
    )
    parser.add_argument(
        '-C', '--cot_host', help='Cursor-on-Target Host or Host:Port',
        required=True
    )
    opts = parser.parse_args()

    spotcot_i = spotcot.SpotCoT(opts.api_key, opts.cot_host, opts.interval)

    try:
        spotcot_i.start()

        while spotcot_i.is_alive():
            time.sleep(0.01)
    except KeyboardInterrupt:
        spotcot_i.stop()
    finally:
        spotcot_i.stop()


if __name__ == '__main__':
    cli()
