#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-11-24 20:35:08
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : https://www.zdaye.com/dayProxy.html 从站大爷网站获取代理IP

# 整个网站有点奇怪，使用requests访问会被屏蔽，所以使用selenium模拟访问

import os
import sys
import browseragents
import requests
import datetime
import re
import time
import random
from selenium import webdriver
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def get_newest_url():
    try:
        head = {'User-Agent': browseragents.get_random_user_agent(), 'Connection': 'keep-alive'}
        data = requests.get('https://www.zdaye.com/dayProxy.html', headers=head, verify=False).text

        for line in data.split('\n'):
            url_result = re.search('.*/dayProxy/ip/([0-9]*).html.*', line)
            if url_result:
                return 'https://www.zdaye.com/dayProxy/ip/{0}.html'.format(url_result.groups()[0])
    except Exception as e:
        raise e
        print("get_newest_url error!")

def selenium_get_newest_url():
    try:
        browser = webdriver.Firefox()
        browser.get("https://www.zdaye.com/dayProxy.html")
        time.sleep(random.uniform(5.18, 7.26))
        a_list = browser.find_elements_by_xpath('//H3//a')
        target_url  =''
        for element in a_list:
            target_url = element.get_attribute('href')
            break
        browser.quit()
        return target_url
    except Exception as e:
        raise e
        print("get_newest_url error!")

def generate_proxies():
    proxies_list = []
    try:
        head = {'User-Agent': browseragents.get_random_user_agent(), 'Connection': 'keep-alive'}
        data = requests.get(selenium_get_newest_url(), headers=head, verify=False).text
        print(data)
        for line in data.split('\n'):
            url_result = re.search('.*([0-9]+?\.[0-9]+?\.[0-9]+?\.[0-9]+?</a>:[0-9]+?)@.*', line)
            #print(line)
            if url_result:
                print(url_result.groups())
                break
    except Exception as e:
        raise e
        print("generate_proxies error!")
    finally:
        pass

def selenium_generate_proxies():
    ipport_list = []
    try:
        browser = webdriver.Firefox()
        browser.get("https://www.zdaye.com/dayProxy.html")
        time.sleep(random.uniform(5.18, 7.26))
        a_list = browser.find_elements_by_xpath('//H3//a')
        for element in a_list:
            browser.get(element.get_attribute('href'))
            break

        ip_content = browser.find_element_by_class_name('cont').get_attribute('innerText')
        ipport_list = re.findall('([0-9]{1,3}\.[0-9]+?\.[0-9]+?\.[0-9]+?:[0-9]*).*', ip_content) or []
        browser.quit()
    except Exception as e:
        raise e
        print("selenuim_generate_proxies error!")
    finally:
        with open('zdayelist.txt', 'w') as file:
            file.write('\n'.join(ipport_list));

def get_proxies(refresh=False):
    if refresh: selenium_generate_proxies()
    with open('zdayelist.txt', 'r') as file:
        data = file.read();
        return data.split("\n")

if __name__ == '__main__':
    print(selenium_generate_proxies())
