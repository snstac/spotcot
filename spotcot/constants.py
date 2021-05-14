#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Spot Cursor-on-Target Constants."""

import logging
import os

__author__ = "Greg Albrecht W2GMD <oss@undef.net>"
__copyright__ = "Copyright 2021 Orion Labs, Inc."
__license__ = "Apache License, Version 2.0"


if bool(os.environ.get('DEBUG')):
    LOG_LEVEL = logging.DEBUG
    logging.debug('spotcot Debugging Enabled via DEBUG Environment Variable.')
else:
    LOG_LEVEL = logging.INFO

LOG_FORMAT = logging.Formatter(
    ('%(asctime)s spotcot %(levelname)s %(name)s.%(funcName)s:%(lineno)d '
     ' - %(message)s'))

# How long between checking for new messages at the Spot API?
DEFAULT_POLL_INTERVAL: int = 120

# Base URL for Spot Feed
SPOT_BASE_URL = "https://api.findmespot.com/spot-main-web/consumer/rest-api/2.0/public/feed/"

DEFAULT_COT_STALE: int = 600
DEFAULT_COT_TYPE: str = "a-.-G-E-V-C"