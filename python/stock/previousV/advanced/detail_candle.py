#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-9-29 14:52:44
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : draw a candlestick with tendency line

import math
import mpl_finance as mpf
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import klineanalyze
import klinedata

def add_annotate(stock_code, key_type, xlist, ylist):
    listlen = len(xlist)
    for n in range(listlen):
        plt.annotate(r'({0}, {1})'.format(xlist[n], round(ylist[n],2)),
             xy=(xlist[n], ylist[n]),  xycoords='data',
             xytext=(-21, +0), textcoords='offset points', fontsize=7)

    plt.title(stock_code + '-' + key_type + '-line')
    #plt.xlabel("date")
    plt.ylabel("price")

def add_guides(stock_code, key_type, low_quotes, high_quotes):
    # get point data
    xlist, ylist = klineanalyze.tendency(low_quotes, high_quotes);
    plt.plot(xlist, ylist, color='b', linewidth=0.6, linestyle="--")
    # print(xlist)
    # print(ylist)

    # smooth
    xlist, ylist = klineanalyze.smooth(xlist, ylist);
    plt.plot(xlist, ylist, color='y')

    # print(xlist)
    # print(ylist)
    add_annotate(stock_code, key_type, xlist, ylist)

def draw_candlestick_on_ax(ax, stock_code, key_type, need_update, key_count=73):
        key_quotes,date_quotes,low_quotes,high_quotes = klinedata.load_klinedata(stock_code, 
            key_type, need_update, key_count)
        mpf.candlestick_ohlc(ax, key_quotes, colordown='#53c156', colorup='#ff1717', 
            width=0.2, alpha=1) #colordown='#F5F5F5', colorup='#DCDCDC'

        # #https://matplotlib.org/examples/pylab_examples/date_index_formatter.html
        class MyFormatter(ticker.Formatter):
            def __init__(self, fmt='%Y-%m-%d %H:%M'):
                self.fmt = fmt

            def __call__(self, x, pos=0): #x就是x轴的刻度数值，但是是浮点数
                if x<0 or x>=len(date_quotes):
                    return ''

                # slice seconds
                return date_quotes[int(x)][:-3] if date_quotes[int(x)][-3:-2] == ':' else date_quotes[int(x)]

        # set xaxix format
        formatter = MyFormatter(date_quotes)
        ax.xaxis.set_major_formatter(formatter)
        ax.xaxis.set_major_locator(ticker.MultipleLocator(len(date_quotes)//4)) # 根据数据量控制间隔

        for label in ax.get_xticklabels():
            label.set_horizontalalignment('center')

        add_guides(stock_code, key_type, low_quotes, high_quotes)


def draw_single_candlestick(stock_code, key_type, need_update, key_count=73):
    fig, ax = plt.subplots(figsize=(800/72, 450/72))
    fig.subplots_adjust(bottom=0.1)
    draw_candlestick_on_ax(ax, stock_code, key_type, need_update, key_count);
    plt.show()

def draw_multiple_candlestick(stock_code, key_type_list, need_update, key_count=73):
    type_len = len(key_type_list)
    plt.figure(num='K analyze', figsize=(18, 9))
    #fig, ax_array = plt.subplots(2, 2, figsize=(16, 9))
    #fig.subplots_adjust(bottom=0.1)

    for n in range(type_len):
        ax = plt.subplot(math.ceil(type_len/2), 2, n+1)
        key_type = key_type_list[n]
        draw_candlestick_on_ax(ax, stock_code, key_type, need_update, key_count);
    plt.show()

if __name__ == '__main__':
    stock_code = '600588'
    stock_code = '002108'
    stock_code = '601611'
    key_type = 'D'
    key_type_list = ['5', '30', 'D', 'W']
    if False:
        draw_single_candlestick(stock_code, key_type, False)
    else:
        draw_multiple_candlestick(stock_code, key_type_list, True)