#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-11-21 14:48:08
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : use selenium to visit csdn and collect article list

import time
import random
from selenium import webdriver

article_list_main_url='https://blog.csdn.net/albertsh/article/list/{0}?t=1&'
article_detail_main_url='https://blog.csdn.net/albertsh/article/details/{0}\n'

def get_csdn_pv(browser_obj):
    try:
        dl_list = browser.find_elements_by_class_name('text-center')
        for element in dl_list:
            if '访问' in element.text:
                return element.get_attribute('title')
    except:
        return 0


def collect_article_url_list(max_page):
    try:
        with open('articlelist.txt', 'w', encoding='utf-8') as outfile:
            browser = webdriver.Firefox()
            for n in range(max_page):
                browser.get(article_list_main_url.format(n+1))
                time.sleep(random.uniform(6.18, 8.26)) # wait page open

                div_list = browser.find_elements_by_class_name('article-item-box')
                for element in div_list:
                    entrance = element.get_attribute('data-articleid')
                    outfile.write(article_detail_main_url.format(entrance))
    except Exception as e:
        raise e
        return False
    else:
        return True

if __name__ == '__main__':
    print(collect_article_url_list(10))