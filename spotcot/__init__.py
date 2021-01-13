#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Spot to Cursor-on-Target Gateway.

"""
Spot to Cursor-on-Target Gateway.
~~~~

:author: Greg Albrecht W2GMD <oss@undef.net>
:copyright: Copyright 2021 Orion Labs, Inc.
:license: Apache License, Version 2.0
:source: <https://github.com/ampledata/spotcot>
"""

from .constants import (LOG_FORMAT, LOG_LEVEL, QUERY_INTERVAL,  # NOQA
                        SPOT_BASE_URL, DEFAULT_STALE)

from .functions import spot_to_cot, hello_event  # NOQA

from .classes import SpotWorker  # NOQA

__author__ = "Greg Albrecht W2GMD <oss@undef.net>"
__copyright__ = "Copyright 2021 Orion Labs, Inc."
__license__ = "Apache License, Version 2.0"
