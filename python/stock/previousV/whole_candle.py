#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-9-26 20:23:16
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : draw a candle

import datetime
import numpy as np
import pandas as pd
import tushare as ts
import mpl_finance as mpf
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import matplotlib.ticker as ticker
from matplotlib.ticker import Formatter


stock_code = '600588'

def update_stock_data():
    df = ts.get_hist_data(stock_code, ktype='5')
    df.to_csv(stock_code+'.csv', columns=['open','high','low','close'])

def draw_candle():
    csv_data = pd.read_csv(stock_code+'.csv', low_memory = False)#防止弹出警告
    dfcvs = pd.DataFrame(csv_data)
    dfcvs.sort_values(by='date', ascending=True, inplace=True)

    interval_quotes = [tuple([i]+list(quote[1:])) for i,quote in enumerate(dfcvs.values)]
    date_quotes = dfcvs.date.values;
    #print(interval_quotes)
    #print(date_quotes)

    fig, ax = plt.subplots(figsize=(800/72, 450/72))
    fig.subplots_adjust(bottom=0.1)
    mpf.candlestick_ohlc(ax, interval_quotes, colordown='#53c156', colorup='#ff1717', width=0.2, alpha=1)

    # #https://matplotlib.org/examples/pylab_examples/date_index_formatter.html
    class MyFormatter(Formatter):
        def __init__(self, fmt='%Y-%m-%d %H:%M'):
            self.fmt = fmt

        def __call__(self, x, pos=0): #x就是x轴的刻度数值，但是是浮点数
            if x<0 or x>=len(date_quotes):
                return ''
            return date_quotes[int(x)][:-3] # slice seconds

    # set xaxix format
    formatter = MyFormatter(date_quotes)
    ax.xaxis.set_major_formatter(formatter)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(len(date_quotes)//4)) # 根据数据量控制间隔

    for label in ax.get_xticklabels():
        #label.set_rotation(45)
        label.set_horizontalalignment('center')

    plt.show()


if __name__ == '__main__':
    update_stock_data()
    draw_candle()