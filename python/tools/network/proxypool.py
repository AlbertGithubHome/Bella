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

import time
import requests
from lxml import etree
from agentpool import agentpool

class proxypool(object):
    def __init__(self, init_url = 'https://www.xicidaili.com/nn/', ip_type_list=['HTTPS']):
        self.proxy_info_page = init_url
        self.ip_type_list = ip_type_list
        self.proxy_list = []
        self.proxy_count = 0
        self.agent_pool = agentpool()

    def get_proxy_list(self):
        self.proxy_count = 0
        headers={"User-Agent": self.agent_pool.get_random_user_agent()}
        response = requests.get(self.proxy_info_page, headers=headers)
        if response.status_code != 200:
            return self.proxy_list

        # 解析代理IP地址和端口
        dom = etree.HTML(response.text)
        ip_list = dom.xpath('//*[@id="ip_list"]/tr[/]/td[2]//text()')
        port_list = dom.xpath('//*[@id="ip_list"]/tr[/]/td[3]//text()')
        type_list = dom.xpath('//*[@id="ip_list"]/tr[/]/td[6]//text()')

        for ip, port, ip_type in zip(ip_list, port_list, type_list):
            if ip_type in self.ip_type_list:
                try:
                    if ip_type == 'HTTP':
                        proxies = {"http": ip + ":" + port}
                        response = requests.get('http://icanhazip.com', proxies=proxies, timeout=2)
                    else:
                        proxies = {"https": ip + ":" + port}
                        response = requests.get('https://icanhazip.com', proxies=proxies, timeout=2)

                    if response.status_code == 200:
                        if response.text.strip().replace('\n', '') == ip:
                            self.proxy_count += 1
                            print(response.text)
                            print("[Info] 成功获取代理{},现在所存代理数为{}".format(proxies, self.proxy_count))
                except:
                    continue
        return self.proxy_list

if __name__ == '__main__':
    pool = proxypool()
    print(pool.get_proxy_list())