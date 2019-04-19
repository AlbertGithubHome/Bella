#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-4-18 15:18:28
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : 学习网络代理的使用，提供获取代理地址的的方法

import requests
import random
import re

#regex_ip_port_src = '<td data-title="IP">183.148.135.58</td>das<td data-title="PORT">9999</td>'
#regex_ip_port = r'<td data-title="IP">([.0-9]+?)</td>.*?<td data-title="PORT">(\d+)</td>'
#print(re.findall(r'^ddasfasdfjaskdf(\d)', 'ddasfasdfjaskdf43fasdjl'))
regex_ip = re.compile(r'<td data-title="IP">([.0-9]+?)</td>')
regex_port = re.compile(r'<td data-title="PORT">(\d+)</td>')

def get_proxies():
    proxies_list = []
    try:
        html_content = requests.get('https://www.kuaidaili.com/free/inha/' + str(random.randint(1, 12))).content.decode('utf-8')
        ip_list = regex_ip.findall(html_content)
        port_list = regex_port.findall(html_content)
        #print(ip_list, len(ip_list), port_list, len(port_list))
        for ip_port in zip(ip_list, port_list):
            proxies_list.append(ip_port[0] + ':' + ip_port[1])
        return proxies_list
    except:
        print("get proxy ip error!")
        proxies_list.append('125.126.203.37:9999');
        return

if __name__ == '__main__':
    print(get_proxies())