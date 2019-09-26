#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-9-24 20:13:26
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : draw a picture about stock

import numpy as np
import pandas as pd
import mpl_finance as mpf
import matplotlib.pyplot as plt
import matplotlib.dates as dates
from matplotlib.ticker import Formatter

# create dataframe with list
dfcvs = pd.DataFrame([
    ["2019/09/17-10:34", 3646, 3650,3644,3650],
    ["2019/09/17-10:35", 3650, 3650,3648,3648],
    ["2019/09/17-10:36", 3650, 3650,3648,3650],
    ["2019/09/17-10:39", 3652, 3654,3648,3652]
],
columns = ['time','open','high','low','close'])

# adjust time format
dfcvs['time']= pd.to_datetime(dfcvs['time'], format="%Y/%m/%d-%H:%M")
dfcvs['time']= dfcvs['time'].apply(lambda x:dates.date2num(x)*1440) #1440=24*60，转换成分钟整数
#print(dfcvs)

# FutureWarning: Method .as_matrix will be removed in a future version. Use .values instead.
# data_matrix = dfcvs.as_matrix()
# convert to matrix
data_matrix = dfcvs.values
print(data_matrix)

fig, ax = plt.subplots(figsize=(800/72, 600/72))

fig.subplots_adjust(bottom=0.1)
mpf.candlestick_ohlc(ax, data_matrix, colordown='#53c156', colorup='#ff1717', width=0.2, alpha=1)

#https://matplotlib.org/examples/pylab_examples/date_index_formatter.html
class MyFormatter(Formatter):
    def __init__(self, dates, fmt='%Y-%m-%d %H:%M'):
        self.dates = dates
        self.fmt = fmt

    def __call__(self, x, pos=0):
        'Return the label for time x at position pos'
        ind = int(np.round(x))
        #ind就是x轴的刻度数值，不是日期的下标
        return dates.num2date(ind/1440).strftime(self.fmt)

# set xaxix format
formatter = MyFormatter(data_matrix[:,0])
ax.xaxis.set_major_formatter(formatter)

for label in ax.get_xticklabels():
    label.set_rotation(45)
    label.set_horizontalalignment('right')

plt.show()



# 运行结果
'''

'''