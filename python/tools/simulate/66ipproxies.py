#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-11-24 21:36:22
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : http://www.66ip.cn/ 从66代理上获取代理ip地址

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

        for line in data.split('\n'):
            ip_result = re.findall('<td>([0-9]+?\.[0-9]+?\.[0-9]+?\.[0-9]+?)</td><td>([0-9]*)</td>', line)
            if len(ip_result) > 0:
                ip_list = [x[0]+':'+x[1] for x in ip_result][0:2]
                break;
    except Exception as e:
        raise e
        print("get_part_proxies error!")
    finally:
        return ip_list

def generate_proxies():
    proxies_list = []
    with open('66iplist.txt', 'w') as file:
        for x in range(30):
            part_list = get_part_proxies('http://www.66ip.cn/areaindex_{0}/1.html'.format(x+1));
            proxies_list.extend(part_list)
            print(x)
            time.sleep(random.uniform(0.18, 0.56))
        file.write('\n'.join(proxies_list));

def get_proxies(refresh=False):
    if refresh: generate_proxies()
    with open('66iplist.txt', 'r') as file:
        data = file.read();
        return data.split("\n")

if __name__ == '__main__':
    print(generate_proxies())