#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 19:18:27 2021

@author: DactylicOrange
"""
from requests import Request, Session
import json
import pprint
import math

trillion = 1000000000000

url = ('https://pro-api.coinmarketcap.com/v1/global-metrics/quotes/latest')


parameters = {
   

    
    }

headers = {
    'Accepts':'application/json',
    'X-CMC_PRO_API_KEY':'YOURAPIKEY'
}

session = Session()
session.headers.update(headers)
#In Python, to print 2 decimal places we will use str. format() with “{:. 2f}” as string and float as a number. 
response = session.get(url, params=parameters)
market_cap = ((json.loads(response.text)['data']['quote']['USD']['total_market_cap']/trillion))

print(float(str(round(market_cap, 2))), end = "T")


print("")
print("GLOBAL CRYPTO MARKETCAP 24h %CHANGE:")
pprint.pprint(json.loads(response.text)['data']['quote']['USD']['total_market_cap_yesterday_percentage_change'])