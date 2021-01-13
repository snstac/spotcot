#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Spot Cursor-on-Target Gateway Functions."""

import datetime

import pycot

import spotcot.constants

__author__ = "Greg Albrecht W2GMD <oss@undef.net>"
__copyright__ = "Copyright 2021 Orion Labs, Inc."
__license__ = "Apache License, Version 2.0"


def spot_to_cot(response, stale: int = None) -> pycot.Event:
    """
    Converts an Spot Response to a Cursor-on-Target Event.
    """
    message = response["feedMessageResponse"]["messages"]["message"][0]

#    time = datetime.datetime.now(datetime.timezone.utc)
    time = datetime.datetime.fromtimestamp(message["unixTime"])
    stale = stale or spotcot.DEFAULT_STALE

    lat = message.get("latitude")
    lon = message.get("longitude")

    if lat is None or lon is None:
        return None

    cot_type = "a-.-G-E-V-C"
    name = message.get("messengerName")
    callsign = name

    point = pycot.Point()
    point.lat = lat
    point.lon = lon
    point.ce = "9999999.0"
    point.le = "9999999.0"
    point.hae = "9999999.0"

    uid = pycot.UID()
    uid.Droid = name

    contact = pycot.Contact()
    contact.callsign = callsign

    remarks = pycot.Remarks()
    _remarks = (
        f"batteryState: {message.get('batteryState')} "
        f"messengerId: {message.get('messengerId')} "
        f"modelId: {message.get('modelId')}"
    )
    remarks.value = _remarks


    detail = pycot.Detail()
    detail.uid = uid
    detail.contact = contact
    detail.remarks = remarks

    event = pycot.Event()
    event.version = "2.0"
    event.event_type = cot_type
    event.uid = f"Spot.{name}"
    event.time = time
    event.start = time
    event.stale = time + datetime.timedelta(seconds=stale)
    event.how = "m-g"
    event.point = point
    event.detail = detail

    return event


def hello_event():
    time = datetime.datetime.now(datetime.timezone.utc)
    name = 'spotcot'
    callsign = 'spotcot'

    uid = pycot.UID()
    uid.Droid = name

    contact = pycot.Contact()
    contact.callsign = callsign

    detail = pycot.Detail()
    detail.uid = uid
    detail.contact = contact

    event = pycot.Event()
    event.version = '2.0'
    event.event_type = 'a-u-G'
    event.uid = name
    event.time = time
    event.start = time
    event.stale = time + datetime.timedelta(hours=1)
    event.how = 'h-g-i-g-o'
    event.detail = detail

    return event
