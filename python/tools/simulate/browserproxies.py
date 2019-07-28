#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-7-28 21:42:48
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : 学习网络代理的使用，提供可用的代理配置

import os
import sys
cur_path = os.path.dirname(__file__) + '\\'

sys.path.append(cur_path)
import browseragents
import requests
import datetime
import re

def archive_proxies(is_https=True, save=True):
    target_url = 'https://www.xicidaili.com/wn/' if is_https else 'https://www.xicidaili.com/wt/'
    proxies_list = []

    try:
        head = {'User-Agent': browseragents.get_random_user_agent(), 'Connection': 'keep-alive'}
        data = requests.get(target_url, headers=head).text

        line_list = data.split('\n');
        line_count = len(line_list)
        count = 0
        while count < line_count:
            ip_result = re.search('.*.*<td>([0-9]+?\.[0-9]+?\.[0-9]+?\.[0-9]+?)</td>.*', line_list[count])
            if ip_result:
                port_result = re.search('.*<td>([0-9]+?)</td>.*', line_list[count+1])
                if port_result:
                    proxies_list.append(ip_result.groups()[0]+':'+port_result.groups()[0])
                count += 1     
            count += 1
    except:
        print("get proxy ip error!")
    finally:
        result_num = len(proxies_list)
        if not save:
            print(proxies_list)
            print(result_num)
        else:
            count = 1
            date_str = datetime.datetime.now().strftime('%Y-%m-%d');
            with open(cur_path+'proxieslist_'+date_str+'.txt', 'w') as file:
                for line in proxies_list:
                    file.write(count == result_num and line or line+'\n')
                    count +=1


def update_proxies():
    archive_proxies(True, True)

def get_proxies(refresh=False):
    if refresh: archive_proxies(True, True)

    date_str = datetime.datetime.now().strftime('%Y-%m-%d');
    with open(cur_path+'proxieslist_'+date_str+'.txt', 'r') as file:
        data = file.read();
        return data.split("\n")

#print(get_proxies())
