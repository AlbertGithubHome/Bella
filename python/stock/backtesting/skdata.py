#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2025-7-26 18:42:48
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : download stock data from tushare

from datetime import datetime, timedelta
from dotenv import load_dotenv
import tushare as ts
import os

#https://tushare.pro/user/token 获取
#ts.set_token('11b0b54fc47e99ed0127a63ed000445be3570639c900739894eaf721')
load_dotenv()
ts.set_token(os.getenv("TUSHARE_TOKEN"))
pro = ts.pro_api()

'''
从tushare下载日线数据
'''
def download_daily_data(code, start_date, end_date):
    print('ready to download [{0}] data between [{1} ~ {2}].'.format(code, start_date, end_date))
    df = pro.daily(ts_code=code, start_date=start_date, end_date=end_date)
    df.to_csv(f'data/{code}.csv')

'''
下载最近N天K线数据
'''
def download_last_ndays_data(code, days):
    # 获取今天的日期
    today = datetime.today()
    # 计算N天前的日期
    one_year_ago = today - timedelta(days=days)
    # 下载数据
    download_daily_data(code, one_year_ago.strftime('%Y%m%d'), today.strftime('%Y%m%d'))

'''
下载最近1年K线数据
'''
def download_last_year_data(code):
    # 下载最近一年的数据
    download_last_ndays_data(code, 366)

# download_daily_data('600644.SH', '20240324', '20250726')
# download_last_year_data('600644.SH')