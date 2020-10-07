#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Spot to Cursor-on-Target Gateway.

"""
Spot to Cursor-on-Target Gateway.
~~~~


:author: Greg Albrecht W2GMD <oss@undef.net>
:copyright: Copyright 2020 Orion Labs, Inc.
:license: Apache License, Version 2.0
:source: <https://github.com/ampledata/spotcot>

"""

from .constants import (LOG_FORMAT, LOG_LEVEL, DEFAULT_COT_PORT,  # NOQA
                        QUERY_INTERVAL)

from .functions import (spot_to_cot, create_spot_feed, get_full_addr,  # NOQA
                        get_first_message)

from .classes import SpotCoT  # NOQA

__author__ = 'Greg Albrecht W2GMD <oss@undef.net>'
__copyright__ = 'Copyright 2020 Orion Labs, Inc.'
__license__ = 'Apache License, Version 2.0'
