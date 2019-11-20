#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-11-20 21:00:54
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : learn selenium start

import time
from selenium import webdriver

browser = webdriver.Firefox()

browser.get("https://blog.csdn.net/albertsh/article/details/52231311")
time.sleep(10)
for i in range(1, 5):
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(1)