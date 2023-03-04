#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-10-3 09:20:40
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : download klinedata from tushare and load to memory

import pandas as pd
import tushare as ts

def update_stock_data(stock_code, key_type):
    df = ts.get_hist_data(stock_code, ktype=key_type)
    df.to_csv('data/' + stock_code+'-' + key_type + '.csv', columns=['open','high','low','close'])

def load_show_data(stock_code, key_type, key_count=73):
    csv_data = pd.read_csv('data/' + stock_code+'-' + key_type + '.csv', low_memory = False) #防止弹出警告
    dfcvs = pd.DataFrame(csv_data)
    dfcvs = dfcvs[:key_count]
    dfcvs.sort_values(by='date', ascending=True, inplace=True)

    key_quotes = [tuple([i]+list(quote[1:])) for i,quote in enumerate(dfcvs.values)]
    date_quotes = dfcvs.date.values;
    high_quotes = dfcvs.high.values;
    low_quotes = dfcvs.low.values;

    # print(key_quotes)
    # print(date_quotes)
    # print(low_quotes)
    # print(high_quotes)
    return key_quotes,date_quotes,low_quotes,high_quotes

def load_klinedata(stock_code, key_type, need_update=True, key_count=73):
    if need_update:
        update_stock_data(stock_code, key_type)
    return load_show_data(stock_code, key_type, key_count)

def load_stock_map():
    stock_map = {}
    with open('data/stocklist.csv', 'r', encoding='utf-8') as file:
        for line in file:
            if not line:
                continue
            data = line.strip()
            data = data.split(',')
            stock_map[data[0]] = data[1]
    return stock_map

if __name__ == '__main__':
    stock_code = '600588'
    key_type = 'D'
    print(load_klinedata(stock_code, key_type))
    #print(load_stock_map())
    # with open('output', 'w') as file:
    #     data = ts.get_stock_basics()
