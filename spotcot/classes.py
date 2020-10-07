#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Spot Cursor-on-Target Class Definitions."""

import logging
import socket
import sys
import threading
import time
import typing

import spotcot

__author__ = 'Greg Albrecht W2GMD <oss@undef.net>'
__copyright__ = 'Copyright 2020 Orion Labs, Inc.'
__license__ = 'Apache License, Version 2.0'


class SpotCoT(threading.Thread):

    """Spot Cursor-on-Target Threaded Class."""

    _logger = logging.getLogger(__name__)
    if not _logger.handlers:
        _logger.setLevel(spotcot.LOG_LEVEL)
        _console_handler = logging.StreamHandler()
        _console_handler.setLevel(spotcot.LOG_LEVEL)
        _console_handler.setFormatter(spotcot.LOG_FORMAT)
        _logger.addHandler(_console_handler)
        _logger.propagate = False

    def __init__(self, api_key: str, cot_host: str, interval: typing.Any) -> None:  # NOQA
        self.api_key = api_key
        self.cot_host = cot_host
        self.interval = interval or spotcot.QUERY_INTERVAL
        self.full_addr = spotcot.get_full_addr(cot_host)

        # Thread Management:
        threading.Thread.__init__(self)
        self._stopped = False

    def stop(self) -> bool:
        """Stops a SpotCot Thread (at the next opportunity)."""
        self._stopped = True
        return self._stopped

    def run(self) -> None:
        """Starts a SpotCoT Thread."""
        spot_feed = spotcot.create_spot_feed(self.api_key)
        self._logger.info("SpotCoT running against CoT Host %s", self.cot_host)

        while 1:
            try:
                spot_feed.collect()
            except spot_sdk.SpotSDKError as exc:
                self._logger.warn(
                    'spot_sdk.collect() threw an Exception (ignored): ')
                self._logger.exception(exc)

            if spot_feed.count() > 0 and spot_feed.messages is not []:
                self.send_cot(spot_feed)

            self._logger.debug('Sleeping for %s seconds...', self.interval)
            time.sleep(self.interval)

    def send_cot(self, spot_feed):
        """Sends an Spot message in CoT format to a remote host using UDP."""
        first_message: Object = spotcot.get_first_message(spot_feed)

        self._logger.debug('First Spot Message: ')
        self._logger.debug(first_message)

        cot_event: Object = spotcot.spot_to_cot(first_message)
        if cot_event is None:
            return

        rendered_event: str = cot_event.render(
            encoding='UTF-8', standalone=True)
        if rendered_event is None:
            return

        self._logger.debug(
            'Sending %s char CoT Event to %s: ',
            len(rendered_event),
            self.full_addr
        )
        self._logger.debug(rendered_event)

        cot_socket: socket.socket = socket.socket(
            socket.AF_INET, socket.SOCK_DGRAM)

        try:
            return cot_socket.sendto(rendered_event, self.full_addr)
        except sys.audit as exc:
            self._logger.debug(
                'Sending CoT Event raised an Exception (ignored): ')
            self._logger.exception(exc)
            return
