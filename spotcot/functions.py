#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Spot Cursor-on-Target Gateway Functions."""

import datetime
import os
import platform

import xml.etree.ElementTree

import pytak

import spotcot.constants

__author__ = "Greg Albrecht W2GMD <oss@undef.net>"
__copyright__ = "Copyright 2021 Orion Labs, Inc."
__license__ = "Apache License, Version 2.0"


def spot_to_cot(response, cot_stale: int = None, cot_type: str = None) -> str:
    """
    Converts an Spot Response to a Cursor-on-Target Event.
    """
    message = response["feedMessageResponse"]["messages"]["message"][0]

    lat = message.get("latitude")
    lon = message.get("longitude")
    if lat is None or lon is None:
        return None

    #   time = datetime.datetime.now(datetime.timezone.utc)
    time = datetime.datetime.fromtimestamp(message["unixTime"])

    # We want to use localtime + stale instead of lastUpdate time + stale
    # This means a device could go offline and we might not know it?
    _cot_stale = int(cot_stale or spotcot.DEFAULT_COT_STALE)
    cot_stale = (datetime.datetime.now(datetime.timezone.utc) + \
                datetime.timedelta(seconds=_cot_stale)).strftime(pytak.ISO_8601_UTC)

    cot_type = cot_type or spotcot.DEFAULT_COT_TYPE

    name = message.get("messengerName")
    callsign = name

    point = xml.etree.ElementTree.Element("point")
    point.set("lat", str(lat))
    point.set("lon", str(lon))
    point.set("hae", "9999999.0")
    point.set("ce", "9999999.0")
    point.set("le", "9999999.0")

    uid = xml.etree.ElementTree.Element("UID")
    uid.set("Droid", name)

    contact = xml.etree.ElementTree.Element("contact")
    contact.set("callsign", str(callsign))

    track = xml.etree.ElementTree.Element("track")
    track.set("course", "9999999.0")

    detail = xml.etree.ElementTree.Element("detail")
    detail.set("uid", name)
    detail.append(uid)
    detail.append(contact)
    detail.append(track)

    remarks = xml.etree.ElementTree.Element("remarks")

    _remarks = (
        f"batteryState: {message.get('batteryState')} "
        f"messengerId: {message.get('messengerId')} "
        f"modelId: {message.get('modelId')} "
        f"(via spotcot@{platform.node()})"
    )

    detail.set("remarks", _remarks)
    remarks.text = _remarks
    detail.append(remarks)

    root = xml.etree.ElementTree.Element("event")
    root.set("version", "2.0")
    root.set("type", cot_type)
    root.set("uid", f"Spot-{name}")
    root.set("how", "m-g")
    root.set("time", time.strftime(pytak.ISO_8601_UTC))
    root.set("start", time.strftime(pytak.ISO_8601_UTC))
    root.set("stale", cot_stale)
    root.append(point)
    root.append(detail)

    return xml.etree.ElementTree.tostring(root)