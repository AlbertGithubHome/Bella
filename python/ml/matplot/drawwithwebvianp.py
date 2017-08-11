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
    stock_price_url = 'https://hk.finance.yahoo.com/chart/TSLA#eyJtdWx0aUNvbG9yTGluZSI6ZmFsc2UsImJvbGxpbmdlclVwcGVyQ29sb3IiOiIjZTIwMDgxIiwiYm9sbGluZ2VyTG93ZXJDb2xvciI6IiM5NTUyZmYiLCJtZmlMaW5lQ29sb3IiOiIjNDVlM2ZmIiwibWFjZERpdmVyZ2VuY2VDb2xvciI6IiNmZjdiMTIiLCJtYWNkTWFjZENvbG9yIjoiIzc4N2Q4MiIsIm1hY2RTaWduYWxDb2xvciI6IiMwMDAwMDAiLCJyc2lMaW5lQ29sb3IiOiIjZmZiNzAwIiwic3RvY2hLTGluZUNvbG9yIjoiI2ZmYjcwMCIsInN0b2NoRExpbmVDb2xvciI6IiM0NWUzZmYiLCJyYW5nZSI6IjF5In0%3D'
    souce_code = urllib.request.urlopen(stock_price_url).read().decode()
    # stock_price_url = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=10y/csv'

    #print(souce_code)
    stock_data = []
    split_source = souce_code.split('\n')

    #print(souce_code.encode("GBK", 'ignore'))
    for line in split_source:
        split_line = line.split(',')
        if len(split_line) == 6:
            if 'values' not in line:
                stock_data.append(line)
                #print(line.encode("GBK", 'ignore'))

    print(web.get_data_yahoo('AAPL','1/1/2014','20/8/2015'))

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

    #plt.plot_data(date, closep, '-', label='Price')

    plt.xlabel('date')
    plt.ylabel('price')

    plt.title('data from web')
    plt.legend()
    plt.show()


graph_date('TSLA')


