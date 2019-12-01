#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-11-30 21:41:46
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : http://www.89ip.cn/index.html 从89代理上获取代理ip地址

import browseragents
import requests
import re
import time
import random
from selenium import webdriver
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def get_part_proxies(main_url):
    ip_list = []
    try:
        head = {'User-Agent': browseragents.get_random_user_agent(), 'Connection': 'keep-alive'}
        data = requests.get(main_url, headers=head, verify=False).text

        data_list = data.split('\n');
        line_count = len(data_list)
        count = 0
        while count < line_count and count + 2 < line_count:
            ip_result = re.findall('([0-9]+?\.[0-9]+?\.[0-9]+?\.[0-9]+?)', data_list[count])
            if len(ip_result) > 0:
                count = count + 2
                port_result = re.findall('([0-9]+)', data_list[count])
                if len(port_result) > 0:
                    ip_list.append(ip_result[0]+':'+port_result[0])
            count = count + 1
    except Exception as e:
        raise e
        print("get_part_proxies error!")
    finally:
        return ip_list

def generate_proxies():
    proxies_list = []
    with open('89iplist.txt', 'w') as file:
        for x in range(1):
            part_list = get_part_proxies('http://www.89ip.cn/index_{0}.html'.format(x+1));
            print(part_list)
            proxies_list.extend(part_list)
            print(x)
            time.sleep(random.uniform(0.18, 0.56))
        file.write('\n'.join(proxies_list));

def get_proxies(refresh=False):
    if refresh: generate_proxies()
    with open('89iplist.txt', 'r') as file:
        data = file.read();
        return data.split("\n")

if __name__ == '__main__':
    print(generate_proxies())
    print(re.findall('([0-9]+)', '9999        </td>'))