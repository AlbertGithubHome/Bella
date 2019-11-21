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
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
# time.sleep(10)
# for i in range(1, 5):
#     browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
#     time.sleep(1)

#browser.get("https://blog.csdn.net/albertsh/article/details/102938754")

# ele_id=browser.find_element_by_id('fanBox')
# print(type(ele_id))
# print(ele_id.text)
# print(ele_id.get_attribute('textContent'))
# print(ele_id.get_attribute('innerText'))
# print(ele_id.get_attribute('innerHTML'))

def get_csdn_pv(browser_obj):
    try:
        dl_list = browser.find_elements_by_class_name('text-center')
        for element in dl_list:
            if '访问' in element.text:
                return element.get_attribute('title')
    except:
        return 0

print(get_csdn_pv(browser))