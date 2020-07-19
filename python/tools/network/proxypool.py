#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2020-05-23 01:01:48
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : 代理池，获取可用代理IP+PORT
#
# 思路：每次请求从指定地址获取可用IP和PORT

import os
import sys
import time
import requests
from lxml import etree
from agentpool import agentpool

class proxypool(object):
    def __init__(self, init_url = 'https://www.xicidaili.com/nn/', max_count = 50, ip_type_list=['HTTPS']):
        self.proxy_info_page = init_url
        self.ip_type_list = ip_type_list
        self.max_count = max_count
        self.proxy_list = []
        self.proxy_count = 0
        self.show_msg = True
        self.agent_pool = agentpool()

    def get_proxy_info_page(self):
        return self.proxy_info_page

    def extract_valid_data(self, ip, port, ip_type):
        try:
            if ip_type == 'HTTP':
                proxies = {"http": ip + ":" + port}
                response = requests.get('http://icanhazip.com', proxies=proxies, timeout=3)
            else:
                proxies = {"https": ip + ":" + port}
                response = requests.get('https://icanhazip.com', proxies=proxies, timeout=3)

            if response.status_code != 200:
                return False

            if response.text.strip().replace('\n', '') == ip:
                self.proxy_count += 1
                self.proxy_list.append(proxies)
                if self.show_msg:
                    print("[INFO] 成功获取代理{0}，现在得到的代理总数为{1}".format(proxies, self.proxy_count))
                return True
        except:
            return False

    # 从页面内容上提取IP和PORT，并将可用代理保留
    def extract_from_xicidaili(self, html_text):
        dom = etree.HTML(html_text)
        ip_list = dom.xpath('//*[@id="ip_list"]/tr[/]/td[2]//text()')
        port_list = dom.xpath('//*[@id="ip_list"]/tr[/]/td[3]//text()')
        type_list = dom.xpath('//*[@id="ip_list"]/tr[/]/td[6]//text()')

        for ip, port, ip_type in zip(ip_list, port_list, type_list):
            if ip_type in self.ip_type_list:
                self.extract_valid_data(ip, port, ip_type)


    # 从本地文件提取IP和PORT，并将可用代理保留
    def extract_from_localhost(self):
        with open(os.path.dirname(__file__) + '/proxy.dat', 'r', encoding='UTF-8') as file:
            for line in file:
                proxy_info = line.replace('\n', '').split(' ')
                if proxy_info[2] in self.ip_type_list:
                    self.extract_valid_data(proxy_info[0], proxy_info[1], proxy_info[2])

    def get_proxy_list(self, show_msg=True):
        self.proxy_count = 0
        self.show_msg = show_msg

        html_content = ''
        if 'localhost' not in self.proxy_info_page:
            headers={"User-Agent": self.agent_pool.get_random_user_agent()}
            response = requests.get(self.proxy_info_page, headers=headers)
            if response.status_code != 200:
                return self.proxy_list
            html_content = response.text

        # 解析代理IP地址和端口
        if 'xicidaili' in self.proxy_info_page:
            self.extract_from_xicidaili(html_content)
        elif 'localhost' in self.proxy_info_page:
            self.extract_from_localhost()
        else:
            pass

        list_len = len(self.proxy_list)
        list_len = list_len if list_len > 0 else 1

        if list_len < self.max_count:
            self.proxy_list = self.proxy_list * int(self.max_count / list_len + 1)
        return self.proxy_list[:50]

if __name__ == '__main__':
    #pool = proxypool()
    pool = proxypool('localhost')
    proxy_list = pool.get_proxy_list()
    print(proxy_list, len(proxy_list))