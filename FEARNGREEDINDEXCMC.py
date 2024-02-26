#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 19:23:09 2021

@author: DactlicOrange
"""
from requests import Request, Session
import json
import pprint

url = ('https://api.alternative.me/fng/?limit=2')

session = Session()

response = session.get(url)
print("CRYPTO FEAR AND GREED INDEX:")
print(" ")
print("FEAR-GREED VALUE:")
pprint.pprint(json.loads(response.text)['data'][0]['value'])
print("MARKET SENTIMENT:")
pprint.pprint(json.loads(response.text)['data'][0]['value_classification'])

fngVal = (json.loads(response.text)['data'][0]['value'])

count = 0
if int(fngVal) > 65:
    count = count - 1
if int(fngVal) < 35:
    count = count + 1
print(count)

