#!/usr/bin/python
# -*- encoding: utf-8 -*-
__author__ = 'm.malinowski'
"""
Project Bitcoin Course Tip Game

This project was created as a subtask of the Data Science module of the Media Informatics Master course.

Written by Max M., 2020
"""

import requests


def get_btc_price():
    btc_api_url = 'https://blockchain.info/ticker'
    response = requests.get(btc_api_url)
    response_json = response.json()
    print(response_json["USD"]["last"])

    return str(response_json["USD"]["last"])
