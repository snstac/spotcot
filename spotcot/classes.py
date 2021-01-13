#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Spot Cursor-on-Target Class Definitions."""

import aiohttp
import asyncio
import json
import logging
import time
import typing

import pycot
import pytak

import spotcot

__author__ = "Greg Albrecht W2GMD <oss@undef.net>"
__copyright__ = "Copyright 2021 Orion Labs, Inc."
__license__ = "Apache License, Version 2.0"


class SpotWorker(pytak.MessageWorker):

    """Reads Spot Data, renders to CoT, and puts on queue."""

    def __init__(self, event_queue: asyncio.Queue, api_key: str,
                 cot_stale: int = None, poll_interval: int = None,
                 password: int = None):
        super().__init__(event_queue)
        self.api_key = api_key
        self.cot_stale = cot_stale
        self.poll_interval: int = int(poll_interval or
                                      adsbxcot.DEFAULT_POLL_INTERVAL)
        self.spot_url: str = (
            f"{spotcot.SPOT_BASE_URL}{self.api_key}/message.json")

        if password:
            self.params = {"feedPassword": password}
        else:
            self.params = {}

        # Used by spot_to_cot function:
        self.cot_renderer = spotcot.spot_to_cot
        self.cot_classifier = pytak.faa_to_cot_type

    async def handle_response(self, response: list) -> None:
        """Handles the response from the Spot API."""
        event: pycot.Event = spotcot.spot_to_cot(response)
        if event:
            await self._put_event_queue(event)
        else:
            self._logger.debug("Empty CoT Event for response='%s'", response)

    async def _get_spot_feed(self):
        """Gets Spot Feed from API."""
        self._logger.debug("Polling Spot API")
        async with aiohttp.ClientSession() as session:
            response = await session.request(
                method="GET",
                url=self.spot_url,
                params=self.params
            )
            json_resp = await response.json()
            _response = json_resp.get("response")

            if "errors" in _response:
                self._logger.error("Error from Spot API: '%s'", _response)
            else:
                await self.handle_response(_response)

    async def run(self) -> None:
        """Runs this Worker, Reads from Pollers."""
        self._logger.info(
            "Running SpotWorker with Spot API URL: %s", self.spot_url)

        while 1:
            await self._get_spot_feed()
            await asyncio.sleep(self.poll_interval)
