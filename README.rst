spotcot - Spot Cursor-on-Target Gateway.
****************************************

.. image:: docs/ScreenShot2021-01-12at10.49.08AM.png
   :alt: Screenshot of Spot CoT PLI Point in ATAK
   :target: docs/ScreenShot2021-01-12at10.49.08AM.png

The ``spotcot`` Spot Cursor-on-Target Gateway transforms Spot position messages
into Cursor on Target (CoT) Position Location Information (PLI) Points for
display on Situational Awareness (SA) applications such as the Android Team
Awareness Kit (ATAK), WinTAK, RaptorX, et al.


``spotcot`` can be run as a foreground command line application, or can be run
as a background service using a daemon like supervisord.

Usage of this gateway requires a `Spot <https://www.findmespot.com/en-us/>`_ device with service.

Installation
============

To install from this source tree::

    $ git checkout https://github.com/ampledata/spotcot.git
    $ cd spotcot/
    $ python setup.py install

To install from PyPI::

    $ pip install spotcot


Setup
=====

``spotcot`` uses the Spot "XML Feed" feature to retrieve Spot location messages
from the Spot API. To enable the "XML Feed" feature:

1. Login to your Spot account at: https://login.findmespot.com/spot-main-web/auth/login.html
2. In the navigation bar, click "XML Feed", then "Create XML Feed".
3. Enter any value for "XML Feed Name".
4. [optional] If you select "Make XML page private", chose and record a password.
5. Click "Create", record the "XML Feed ID".

Usage
=====

The `spotcot` daemon has several runtime arguments::

    $ spotcot -h
    usage: spotcot [-h] -k API_KEY [-i INTERVAL] -C COT_HOST

    optional arguments:
      -h, --help            show this help message and exit
      -k API_KEY, --api_key API_KEY
                            Spot API Key ("XML Feed Id")
      -i INTERVAL, --interval INTERVAL
                            Spot API Query Interval
      -C COT_HOST, --cot_host COT_HOST
                            Cursor-on-Target Host or Host:Port

For minimum operation, `-k API_KEY` & `-C COT_HOST` are required.

Source
======
Github: https://github.com/ampledata/spotcot

Author
======
Greg Albrecht W2GMD oss@undef.net

http://ampledata.org/

Copyright
=========
Copyright 2021 Orion Labs, Inc.

License
=======
Apache License, Version 2.0. See LICENSE for details.
