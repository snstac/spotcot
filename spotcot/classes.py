#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Spot Cursor-on-Target Class Definitions."""

import aiohttp
import asyncio
import json
import logging
import time
import typing

import pytak

import spotcot

__author__ = "Greg Albrecht W2GMD <oss@undef.net>"
__copyright__ = "Copyright 2021 Orion Labs, Inc."
__license__ = "Apache License, Version 2.0"


class SpotWorker(pytak.MessageWorker):

    """Reads Spot Data, renders to CoT, and puts on queue."""

    def __init__(self, event_queue: asyncio.Queue, opts)
        super().__init__(event_queue)
        self.url: urllib.parse.ParseResult = urllib.parse.urlparse(opts.get("COT_URL"))

        self.cot_stale = opts.get("COT_STALE")
        self.cot_type = opts.get("COT_TYPE") or spotcot.DEFAULT_COT_TYPE

        self.api_key = opts.get("API_KEY")
        self.spot_url: str = (
            f"{spotcot.SPOT_BASE_URL}{self.api_key}/message.json")

        self.poll_interval: int = int(opts.get("POLL_INTERVAL") or spotcot.DEFAULT_POLL_INTERVAL)

        password = opts.get("SPOT_PASSWORD")
        if password:
            self.params = {"feedPassword": password}
        else:
            self.params = {}

        # Used by spot_to_cot function:
        self.cot_renderer = spotcot.spot_to_cot

    async def handle_response(self, response: list) -> None:
        """Handles the response from the Spot API."""
        event: str = spotcot.spot_to_cot(response, self.cot_stale, self.cot_type)
        if event:
            await self._put_event_queue(event)
        else:
            self._logger.debug("Empty CoT Event for response='%s'", response)

    async def _get_spot_feed(self):
        """Gets Spot Feed from API."""
        self._logger.debug("Polling Spot API")

        async with aiohttp.ClientSession() as session:
            try:
                response = await session.request(
                    method="GET",
                    url=self.spot_url,
                    params=self.params
                )
            except Exception as exc:
                self._logger.error("Exception raised while accessing Spot API.")
                self._logger.exception(exc)
                return

            try:
                json_resp = await response.json()
                _response = json_resp.get("response")
            except Exception as exc:
                self._logger.error("Exception raised while parsing Spot API data.")
                self._logger.exception(exc)
                return

            if "errors" in _response:
                self._logger.error("Received error response from Spot API: '%s'", _response)
            elif _response:
                await self.handle_response(_response)
            else:
                self._logger.error("No valid response from Spot API.")

    async def run(self) -> None:
        """Runs this Worker, Reads from Pollers."""
        self._logger.info(
            "Running SpotWorker with Spot API URL: %s", self.spot_url)

        while 1:
            await self._get_spot_feed()
            await asyncio.sleep(self.poll_interval)
