#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-11-22 16:28:13
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : use selenium to random visit csdn article

import time
import random
import pandas
from selenium import webdriver


def get_csdn_pv(browser_obj):
    try:
        dl_list = browser_obj.find_elements_by_class_name('text-center')
        for element in dl_list:
            if '访问' in element.text:
                return element.get_attribute('title')
    except:
        return 0


def random_visit_article(max_count):
    try:
        url_list = get_article_url_list()
        browser = webdriver.Firefox()
        for x in range(max_count):
            #browser.delete_all_cookies()
            target_url = random.choice(url_list)
            browser.get(target_url)
            time.sleep(random.uniform(6.18, 50.26))
            print(target_url, get_csdn_pv(browser), x,
                time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        browser.quit()
    except Exception as e:
        raise e
        return False
    else:
        return True

def get_article_url_list():
    return pandas.read_csv('articlelist.txt', header=None)[0].values.tolist();

if __name__ == '__main__':
    print(random_visit_article(100), "completed")