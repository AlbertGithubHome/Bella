#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-11-24 20:45:23
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : 过滤爬虫得到的代理数据，找到可用的ip代理

import requests

def test_proxy_valid(ip_port):
    # 代理IP地址
    proxy_data = { 'http': ip_port, 'https': ip_port, }

    # 客户端说明
    head_data = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0",
        'Connection': 'keep-alive'
    }

    try:
        response = requests.get('http://icanhazip.com', headers=head_data, proxies=proxy_data)
        outer_ip = response.text.strip().replace('\n', '')
        print(outer_ip, outer_ip == ip)
        return outer_ip == ip
    except:
        return False

def zdaye_proxy_filter():
    data_list = []
    with open('zdayelist.txt', 'r') as file:
        data = file.read();
        data_list = data.split("\n")

    valid_list = []
    for ip_port in data_list:
        if test_proxy_valid(ip_port):
            valid_list.apped(ip_port);

    with open('zdayelist.dat', 'w') as file:
        file.write('\n'.join(valid_list))

def ip66_proxy_filter():
    data_list = []
    with open('66iplist.txt', 'r') as file:
        data = file.read();
        data_list = data.split("\n")

    valid_list = []
    for ip_port in data_list:
        if test_proxy_valid(ip_port):
            valid_list.apped(ip_port);

    with open('66iplist.dat', 'w') as file:
        file.write('\n'.join(valid_list))

if __name__ == '__main__':
    #zdaye_proxy_filter()
    ip66_proxy_filter()

'''
zdaye_proxy_filter() : https://www.zdaye.com/dayProxy.html
ip66_proxy_filter()  : http://www.66ip.cn
'''
