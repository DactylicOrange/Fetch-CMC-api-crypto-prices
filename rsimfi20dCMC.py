#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 17:55:46 2021

@author: DactylicOrange
"""

from requests import Request, Session
import json
import requests 
import numpy as np
import pprint
import matplotlib.pyplot as plt
import datetime as dt
import calendar



#ONLY ISSUE, day 0 should be 20days ago, day 19 is todays so get dates for 
# x axis to start at date for 20 days ago and end at todays date
a = dt.date.today()
numdays = 20
dateList = []
for l in range (0, numdays):
    dateList.append(a - dt.timedelta(days = l))
print(dateList)


#RSI

symbolQuestion = input("BTC or ETH? ")
# Define indicator
indicator = "rsi"
  
# Define endpoint 
endpoint = f"https://api.taapi.io/{indicator}"
# Define a parameters dict for the parameters to be sent to the API 
parameters = {
    # key
    'secret': 'YOUR TAAPI APIKEY',
    'exchange': 'binance',
    'symbol': str(symbolQuestion)+ "/USDT",
    'interval': "1d",
    'backtracks': '20',
    'candles': 'candles'
    } 
session = Session()
# Send get request and save the response as response object 
response = requests.get(url = endpoint, params = parameters)
  
# Extract data in json format 
rsires = response.json()
# Print result
#print(result)
#print(result)if rsiVal > 80:

rsibacks = list(rsires)
#STARTS AT 0 index with backtrack 20 by reversing it
rsibacks.reverse()
# each day for past 20 days
#for i in range(20):
   # print(i, rsires[i])
#for i in range(20):
   #(x,y) = (i,rsibacks[i]['value'])
   #print(x,y)



#graph RSI
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
plt.title("RELATIVE STRENGTH INDEX: past 20d")
plt.xlabel("past<<<DAYS>>>now")
plt.ylabel("RSI")
#GRAPH RSI
plt.yticks(np.arange(0,100,step =10))
plt.xticks(np.arange(0,20,step=1))

#HORIZONTAL Overbought
a = [0, 20]
b = [70, 70]
plt.plot(a, b, color='red')
#HORIZONTAL Oversold
c =[30,30]
plt.plot(a, c, color='green')

for j in range(0,20):
    plt.plot(j,rsibacks[j]["value"],'ko-', label = "RSI VALUES", linewidth=2)

plt.axis([0,20,0,100])


plt.show()






#MFI

indicator = "mfi"
  
# Define endpoint 
endpoint = f"https://api.taapi.io/{indicator}"
# Define a parameters dict for the parameters to be sent to the API 
parameters = {
    #key
    'secret': 'YOURTAAPIKEY',
    'exchange': 'binance',
    'symbol': str(symbolQuestion)+ "/USDT",
    'interval': "1d",
    'backtracks': '20',
    'candles': 'candles'
    } 
# Print result
session = Session()
# Send get request and save the response as response object 
response = requests.get(url = endpoint, params = parameters)
  
# Extract data in json format 
mfires = response.json()
# Print result
mfibacks = list(mfires)

mfibacks.reverse()
#for i in range(20):
   #print(i, mfires[i])
#for i in range(20):
   #(x2,y2) = (i,[mfibacks[i]['value']])



#graph MFI
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
plt.title("MONEY FLOW INDEX: past 20")
plt.xlabel("past<<DAYS>>now")
plt.ylabel("MFI")
plt.yticks(np.arange(0,100,step =10))
plt.xticks(np.arange(0,20,step=1))

#HORIZONTAL Overbought
a = [0, 20]
b = [80, 80]
plt.plot(a, b, color='red')
#HORIZONTAL Oversold
c =[20,20]
plt.plot(a, c, color='green')

for p in range(0,20):
    #mfibacke= mfibacks[p]
    plt.plot(p,mfibacks[p]["value"], color = 'black', marker = 'o', label = "MFI VALUES")
    

plt.axis([0,20,0,100])

plt.show()


