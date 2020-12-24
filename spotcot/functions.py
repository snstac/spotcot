#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Spot Cursor-on-Target Gateway Functions."""

import datetime

import spot_sdk
import pycot

import spotcot.constants

__author__ = 'Greg Albrecht W2GMD <oss@undef.net>'
__copyright__ = 'Copyright 2020 Orion Labs, Inc.'
__license__ = 'Apache License, Version 2.0'


def spot_to_cot(message: spot_sdk.Message) -> pycot.Event:
    """
    Converts an Spot Message to a Cursor-on-Target Event.

    :param message: Spot Message to convert to CoT.
    :type message: `spot_sdk.Message`
    """
    time = datetime.datetime.now()

    lat = message.__getattribute__('latitude')
    lon = message.__getattribute__('longitude')

    if lat is None or lon is None:
        return None

    print(message.raw)
    name = message.raw.get('messengerName')

    point = pycot.Point()
    point.lat = lat
    point.lon = lon
    point.ce = '10'
    point.le = '10'
    point.hae = '10'

    uid = pycot.UID()
    uid.Droid = name

    detail = pycot.Detail()
    detail.uid = uid

    event = pycot.Event()
    event.version = '2.0'
    event.event_type = 'a-f-G-E-V-C'
    event.uid = f"Spot.{name}"
    event.time = time
    event.start = time
    event.stale = time + + datetime.timedelta(hours=1)  # 1 hour expire
    event.how = 'h-e'
    event.point = point
    event.detail = detail

    return event


def create_spot_feed(api_key: str, password: str) -> spot_sdk.Feed:
    """Creates a Spot Message Feed."""
    if not isinstance(password, str):
        return spot_sdk.Feed(api_key)
    else:
        return spot_sdk.Feed(api_key, password)


def get_first_message(spot_feed: spot_sdk.Feed) -> spot_sdk.Message:
    """Gets the first Message from a Spot Feed."""
    first_message = spot_feed.first()
    assert isinstance(first_message, spot_sdk.Message)
    return first_message


def get_full_addr(cot_host: str) -> tuple:
    """Gets the Socket Address for the CoT Destination Host."""
    if ':' in cot_host:
        addr, port = cot_host.split(':')
    else:
        addr = cot_host
        port = spotcot.constants.DEFAULT_COT_PORT
    return addr, int(port)
