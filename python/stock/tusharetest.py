#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-9-26 19:50:36
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : tushare test usage

import numpy as np
import pandas as pd
import tushare as ts
import mpl_finance as mpf
import matplotlib.pyplot as plt
import matplotlib.dates as dates
from matplotlib.ticker import Formatter


#print(ts.get_deposit_rate())
df = ts.get_hist_data('000875', ktype='5')
#直接保存
df.to_csv('000875.csv')

#选择保存
#df.to_csv('c:/day/000875.csv',columns=['open','high','low','close'])

#https://tushare.pro/user/token 获取
ts.set_token('11b0b54fc47e99ed0127a63ed000445be3570639c900739894eaf721')
df = ts.pro_bar(ts_code='000001.SZ', adj='qfq', start_date='20180101', end_date='20181011')
df.to_csv('000001.csv')