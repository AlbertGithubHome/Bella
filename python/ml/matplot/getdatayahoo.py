#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#a test for drawing a plot with web via numpy

__author__ = 'AlbertS'

import pandas_datareader.data as web 



#print(web.get_data_yahoo('AAPL','1/7/2017','2/7/2017'))
#print("test")
#
#import requests
import time
import pandas as pd
import matplotlib.pyplot as plt

def datetime_timestamp(dt):
     time.strptime(dt, '%Y-%m-%d %H:%M:%S')
     s = time.mktime(time.strptime(dt, '%Y-%m-%d %H:%M:%S'))
     return str(int(s))

s = requests.Session()

#Replace B=xxxx
cookies = dict(B='c650m5hchrhii&b=3&s=tk')

#Replace crumb=yyyy
crumb = 'NMhMTCv7QpM'

begin = datetime_timestamp("2014-01-01 09:00:00")

end = datetime_timestamp("2017-04-30 09:00:00")
r = s.get("https://query1.finance.yahoo.com/v7/finance/download/IBM?period1="+begin+"&period2="+end+"&interval=1d&events=history&crumb="+crumb,cookies=cookies,verify=False)

f = open('IBM.csv', 'w')
f.write(r.text)
f.close()    


es = pd.read_csv('IBM.csv', index_col=0,parse_dates=True, sep=",", dayfirst=True)

data = pd.DataFrame({"IBM" : es["Adj Close"][:]}) 

print(data.info())

data.plot(subplots=True, grid=True, style="b", figsize=(8, 6))

plt.show()






