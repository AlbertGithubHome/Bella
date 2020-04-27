#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2020-3-8 17:46:30
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : csdn data statistics

import time
import random
import datetime
from selenium import webdriver

#data_title = ['原创', '粉丝', '获赞', '评论', '访问']
data_title = ['原创', '粉丝', '获赞', '评论', '访问', '积分', '收藏', '周排名', '总排名']
article_main_url='https://blog.csdn.net/albertsh/article/details/104719370'

def get_csdn_title_data(title_name, browser_obj):
    try:
        dl_list = browser_obj.find_elements_by_class_name('text-center')
        for element in dl_list:
            #print(element.text)
            if title_name in element.text:
                return element.get_attribute('title')
    except Exception as e:
        raise e
        return 0

def get_csdn_rank_data(browser_obj):
    try:
        dl_list = browser_obj.find_elements_by_class_name('grade-box')
        for element in dl_list:
            return (element.text.replace('等级:\n', '').replace(':\n', '+').replace('\n', ' ').replace('+', ':'))
            return ''
    except Exception as e:
        raise e
        return ''

def statistics_once():
    try:
        with open('csdn_visit_statistics.txt', 'a', encoding='utf-8') as outfile:
            browser = webdriver.Firefox()
            browser.get(article_main_url)
            time.sleep(random.uniform(6.18, 8.26)) # wait page open
            outfile.write(time.strftime('\n%Y-%m-%d %H:%M:%S  ',time.localtime(time.time())))
            for title_name in data_title:
                log_str = '{0}:{1} '.format(title_name, get_csdn_title_data(title_name, browser))
                outfile.write(log_str)
                print(log_str)
            #log_end_str = get_csdn_rank_data(browser)
            #outfile.write(log_end_str)
            #print(log_end_str)
            browser.quit()

    except Exception as e:
        raise e
        return False
    else:
        return True

if __name__ == '__main__':
    print('execute:', statistics_once())