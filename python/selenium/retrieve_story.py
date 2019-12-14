#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-12-14 10:52:09
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : retrieve story from website

import time
import random
from selenium import webdriver


def story_content(browser_obj, file):
    try:
        #dl_list = browser_obj.find_elements_by_id_name('chaptercontent')#.find_elements_by_xpath('//p')
        #dl_list = browser_obj.find_elements_by_xpath('//div/*')
        dl_list = browser_obj.find_elements_by_id('chaptercontent')
        #print(dl_list)
        for element in dl_list:
            #print(element.text)
            file.write(element.text)
    except:
        return 0


def retrieve_story(url_format, start_page, max_count):
    start = start_page
    sub_suffix = ["", "_2", "_3"]
    try:
        with open('chenzhuang.txt', 'w', encoding='UTF-8') as file:
            browser = webdriver.Firefox()
            for x in range(max_count):
                for i in range(3):
                    target_url = url_format.format(str(start)+sub_suffix[i])
                    browser.get(target_url)
                    time.sleep(random.uniform(1.18, 3.26))
                    print(target_url, story_content(browser, file), x,
                        time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
                start = start + 1
            browser.quit()
    except Exception as e:
        raise e
        return False
    else:
        return True

if __name__ == '__main__':
    print(retrieve_story('https://m.xxxx.com/98/98171/{0}.html', 44067603, 100))