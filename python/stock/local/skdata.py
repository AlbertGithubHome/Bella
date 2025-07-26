#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2025-7-26 18:42:48
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : tushare test usage for download

import tushare as ts
from datetime import datetime, timedelta

#https://tushare.pro/user/token 获取
ts.set_token('11b0b54fc47e99ed0127a63ed000445be3570639c900739894eaf721')
pro = ts.pro_api()

def download_daily_data(code, start_date, end_date):
    print('ready to download [{0}] data between [{1} ~ {2}].'.format(code, start_date, end_date))
    df = pro.daily(ts_code=code, start_date=start_date, end_date=end_date)
    df.to_csv(f'{code}.csv')

def download_last_year_data(code):
    # 获取今天的日期
    today = datetime.today()
    # 计算一年前的日期
    one_year_ago = today - timedelta(days=366)
    # 下载数据
    download_daily_data(code, one_year_ago.strftime('%Y%m%d'), today.strftime('%Y%m%d'))


def download_last_ndays_data(code, days):
    # 获取今天的日期
    today = datetime.today()
    # 计算一年前的日期
    one_year_ago = today - timedelta(days=days)
    # 下载数据
    download_daily_data(code, one_year_ago.strftime('%Y%m%d'), today.strftime('%Y%m%d'))

# download_daily_data('600644.SH', '20240324', '20250726')
# download_last_year_data('600644.SH')