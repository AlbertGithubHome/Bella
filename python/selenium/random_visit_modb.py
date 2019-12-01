#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-11-30 22:41:58
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : use selenium to random visit modb article

import time
import random
import pandas
from selenium import webdriver


def random_visit_article(max_count):
    try:
        url_list = get_article_url_list();
        browser = webdriver.Firefox()
        for x in range(max_count):
            #browser.delete_all_cookies()
            target_url = random.choice(url_list)
            browser.get(target_url)
            time.sleep(random.uniform(3.18, 6.26))
            print(x)
        browser.quit()
    except Exception as e:
        raise e
        return False
    else:
        return True

def get_article_url_list():
    return pandas.read_csv('modbarticlelist.txt', header=None)[0].values.tolist();

if __name__ == '__main__':
    print(random_visit_article(100))