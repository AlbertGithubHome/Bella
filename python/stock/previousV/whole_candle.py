#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-9-26 20:23:16
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : draw a candle

import numpy as np
import pandas as pd
import tushare as ts
import mpl_finance as mpf
import matplotlib.pyplot as plt
import matplotlib.dates as dates
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
    #print(interval_quotes)
    #print(dfcvs.date.values)

    fig, ax = plt.subplots(figsize=(800/72, 450/72))
    fig.subplots_adjust(bottom=0.1)
    mpf.candlestick_ohlc(ax, interval_quotes, colordown='#53c156', colorup='#ff1717', width=0.2, alpha=1)

    # #https://matplotlib.org/examples/pylab_examples/date_index_formatter.html
    # class MyFormatter(Formatter):
    #     def __init__(self, dates, fmt='%Y-%m-%d %H:%M'):
    #         self.dates = dates
    #         self.fmt = fmt

    #     def __call__(self, x, pos=0):
    #         'Return the label for time x at position pos'
    #         ind = int(np.round(x))
    #         #ind就是x轴的刻度数值，不是日期的下标
    #         return dates.num2date(ind/1440).strftime(self.fmt)

    # # set xaxix format
    # formatter = MyFormatter(data_matrix[:,0])
    # ax.xaxis.set_major_formatter(formatter)

    # for label in ax.get_xticklabels():
    #     label.set_rotation(45)
    #     label.set_horizontalalignment('right')

    plt.show()


if __name__ == '__main__':
    #update_stock_data()
    draw_candle()