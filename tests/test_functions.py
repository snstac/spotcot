#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Spot Cursor-on-Target Gateway Function Tests."""

import unittest

import spot_sdk

import spotcot.functions

__author__ = 'Greg Albrecht W2GMD <oss@undef.net>'
__copyright__ = 'Copyright 2020 Orion Labs, Inc.'
__license__ = 'Apache License, Version 2.0'


TEST_RESPONSE = {
    "response": {
        "feedMessageResponse": {
          "count": 2,
          "feed": {
            "id": "0DHc3pHDeJlq4kz6bHx5jW1QfzKlsWt7W",
            "name": "spotcot",
            "description": "spotcot",
            "status": "ACTIVE",
            "usage": 0,
            "daysRange": 7,
            "detailedMessageShown": True,
            "type": "SHARED_PAGE"
          },
          "totalCount": 2,
          "activityCount": 0,
          "messages": {
            "message": [
              {
                "@clientUnixTime": "0",
                "id": 1480220691,
                "messengerId": "0-3032366",
                "messengerName": "gba Spot Gen 3",
                "unixTime": 1601691600,
                "messageType": "UNLIMITED-TRACK",
                "latitude": 37.7599,
                "longitude": -122.49768,
                "modelId": "SPOT3",
                "showCustomMsg": "Y",
                "dateTime": "2020-10-03T02:20:00+0000",
                "batteryState": "GOOD",
                "hidden": 0,
                "altitude": 23
              },
              {
                "@clientUnixTime": "0",
                "id": 1480218901,
                "messengerId": "0-3032366",
                "messengerName": "gba Spot Gen 3",
                "unixTime": 1601691300,
                "messageType": "UNLIMITED-TRACK",
                "latitude": 37.75999,
                "longitude": -122.49779,
                "modelId": "SPOT3",
                "showCustomMsg": "Y",
                "dateTime": "2020-10-03T02:15:00+0000",
                "batteryState": "GOOD",
                "hidden": 0,
                "altitude": -103
              }
            ]
          }
        }
    }
}


class FunctionsTestCase(unittest.TestCase):
    """
    Tests for Functions.
    """

    def test_spot_sdk_message(self):
        """
        Tests that spot_sdk's Message Object imports our JSON Test Message.
        :return:
        """
        first_message = TEST_RESPONSE[
            'response']['feedMessageResponse']['messages']['message'][0]
        spot_sdk_msg = spot_sdk.Message(first_message)
        self.assertEqual(type(spot_sdk_msg), spot_sdk.Message)
        print(spot_sdk_msg)

    def test_spot_to_cot(self):
        """
        Tests that spot_to_cot converts Spot Messages to CoT Events.
        """
        response = TEST_RESPONSE['response']
        raw_messages = response['feedMessageResponse']['messages']['message']
        messages = [spot_sdk.Message(x) for x in raw_messages]
        first_message = messages[0]
        cot_event = spotcot.functions.spot_to_cot(first_message)
        print(cot_event)
        self.assertEqual(cot_event.event_type, 'a-f-G-E-V-C')
        self.assertEqual(cot_event.uid, 'Spot.gba Spot Gen 3')


if __name__ == '__main__':
    unittest.main()
