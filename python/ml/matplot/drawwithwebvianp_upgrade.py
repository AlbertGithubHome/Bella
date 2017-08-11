#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#a test for drawing a plot with web via numpy

__author__ = 'AlbertS'

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import urllib
import pandas_datareader.data as web 

def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter

def graph_date(stock):
    #stock_price_url = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=10y/csv'
    #souce_code = urllib.request.urlopen(stock_price_url).read().decode()
    souce_code = web.get_data_yahoo(stock,'1/1/2014','20/8/2015')
    print(souce_code)

    #date, closep, highp, lowp, openp, volume = np.loadtxt(stock_data, delimiter=',', unpack=True, converters={0: bytespdate2num('%Y%m%d', 'utf-8')})
        # %Y = full year. 2015
        # %y = partial year 15
        # %m = number month
        # %d = number day
        # %H = hours
        # %M = minutes
        # %S = seconds
        # 12-06-2014
        # %m-%d-%Y

    plt.plot_data(souce_code, '-', label='Price')

    plt.xlabel('date')
    plt.ylabel('price')

    plt.title('data from web')
    plt.legend()
    plt.show()


graph_date('AAPL')


