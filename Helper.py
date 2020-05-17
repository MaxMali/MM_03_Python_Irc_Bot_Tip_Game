#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
Project local settings

Written by Max. M., 2020
"""
import requests

def get_btc_price():
    btc_api_url = 'https://blockchain.info/ticker'
    response = requests.get(btc_api_url)
    response_json = response.json()
    print(response_json["USD"]["last"])

    return str(response_json["USD"]["last"])