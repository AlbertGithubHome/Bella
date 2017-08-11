#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#a test for drawing a plot with web via numpy

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import urllib
import pandas_datareader.data as web 

def graph_date(stock):
    stock_price_url = 'https://query1.finance.yahoo.com/v7/finance/download/IBM?period1=1499233035&period2=1501911435&interval=1d&events=history&crumb=d/Vb661AF76'
    souce_code = urllib.request.urlopen(stock_price_url)


#px=web.get_data_yahoo('AAPL')
#px=web.DataReader('F-F_Research_Data_factors','famafrench')  
#print(px)
a='https://query1.finance.yahoo.com/v7/finance/download/IBM?period1=1499232959&period2=1501911359&interval=1d&events=history&crumb=T4azGy7vrDE'
b='https://query1.finance.yahoo.com/v7/finance/download/IBM?period1=1499235132&period2=1501913532&interval=1d&events=history&crumb=d/Vb661AF76'
c='https://query1.finance.yahoo.com/v7/finance/download/IBM?period1=1499235163&period2=1501913563&interval=1d&events=history&crumb=8zcY/16nOTO'
urllib.request.urlretrieve(a, "ibm.csv")