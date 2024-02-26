#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 14:57:15 2021

@author: DactylicOrange
"""

from requests import Request, Session
import json
import pprint




url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

#BITCOIN
parameters = {
   'slug':'bitcoin',
   'convert':'USD',
   
   #'slug':'ethereum',
   #'convert':'USD'
    
    }

headers = {
    'Accepts':'application/json',
    'X-CMC_PRO_API_KEY':'15d36e6d-0aac-4252-b128-bfe53cc2e849'
}

session = Session()
session.headers.update(headers)

response = session.get(url, params=parameters)
print("BTC PRICE:")
print("$", end= "")
pprint.pprint(json.loads(response.text)['data']['1']['quote']['USD']['price'])
print("")


#ETHEREUM
parameters = {
   
   'slug':'ethereum',
   'convert':'USD'
    
    }

response = session.get(url, params=parameters)
print("ETH PRICE:")
print("$", end= "")
pprint.pprint(json.loads(response.text)['data']['1027']['quote']['USD']['price'])
print("")

#ETHEREUM CLASSIC
parameters = {
   
   'slug':'ethereum-classic',
   'convert':'USD'
    
    }

response = session.get(url, params=parameters)
print("ETC PRICE:")
print("$", end= "")
pprint.pprint(json.loads(response.text)['data']['1321']['quote']['USD']['price'])
print("")

#SOL
parameters = {
   
   'slug':'solana',
   'convert':'USD'
    
    }

response = session.get(url, params=parameters)
print("SOL PRICE:")
print("$", end= "")
pprint.pprint(json.loads(response.text)['data']['5426']['quote']['USD']['price'])
print("")

#LITECOIN
parameters = {
   
   'slug':'litecoin',
   'convert':'USD'
    
    }

response = session.get(url, params=parameters)
print("LTC PRICE:")
print("$", end= "")
pprint.pprint(json.loads(response.text)['data']['2']['quote']['USD']['price'])
print("")

#POLKADOT
parameters = {
   
   'slug':'polkadot',
   'convert':'USD'
   
    
    }


response = session.get(url, params=parameters)
print("DOT PRICE:")
print("$", end= "")
pprint.pprint(json.loads(response.text)['data']['6636']['quote']['USD']['price']) 
print("")

#MATIC
parameters = {
   
   'slug':'polygon',
   'convert':'USD'
    
    }


response = session.get(url, params=parameters)
print("MATIC PRICE:")
print("$", end= "")
pprint.pprint(json.loads(response.text)['data']['3890']['quote']['USD']['price']) 
print("")

