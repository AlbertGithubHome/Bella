#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-04-18 13:37:07
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : 学习网络代理的使用

# 查询IP地址：http://www.ip138.com/
# 查询IP子页：http://2019.ip138.com/ic.asp
# 显示IP地址：https://ip.cn/
# 返回IP地址：http://icanhazip.com/

import time
import random
import agents
import proxies
import requests
import targeturls

def start_crawler(max_fail_count=10):
    agents_list = agents.get_user_agents()
    targer_urls = targeturls.get_urls()
    fail_count = 1
    try_count = 1
    with open('crawler_log.txt', 'w') as file:
        while fail_count <= max_fail_count:
            proxies_list = proxies.get_proxies()
            while True:
                try:
                    user_agent = random.choice(agents_list)
                    target_url = random.choice(targer_urls)
                    user_proxy = 'http://' + random.choice(proxies_list)

                    print('try count = {0}, proxy = {1}, url = {2}'.format(try_count, user_proxy, target_url))
                    file.write('try count = {0}, fail count = {1}, proxy = {2}, url = {3}, agent = {4}\n'.format(try_count,
                        fail_count, user_proxy, target_url, user_agent))

                    html_response = requests.get(target_url, proxies={'http': user_proxy, 'https': user_proxy},
                        headers={'User-Agent': user_agent,
                                'Connection': 'keep-alive' })

                    try_count += 1
                    with open("target.html", "wb") as page:
                        page.write(html_response.content)
                    time.sleep(random.uniform(1.1, 3.3))
                    pass
                except:
                    print('failed!')
                    break
            fail_count += 1

def tmpstart(ip, proxy_ip):
    html_response = requests.get(ip, proxies={'http': proxy_ip, 'https': proxy_ip},
         headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
                 'Connection': 'keep-alive'})
    with open('zip.txt', 'wb') as file:
        file.write(html_response.content)

def singlestart():
    '''代理IP地址（高匿）'''
    proxy = {
        'http': 'http://111.177.171.195:9999',
        'https': 'http://111.177.171.195:9999'
    }
    '''head 信息'''
    head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
                 'Connection': 'keep-alive'}
    '''http://icanhazip.com会返回当前的IP地址'''
    p = requests.get('http://icanhazip.com', headers=head, proxies=proxy)
    print(p.text)

if __name__ == '__main__':
    #start_crawler()
    singlestart()
    #tmpstart('http://icanhazip.com/', '115.159.201.179:80')


# headers = {
#     # "Host": "blog.csdn.net",
#     "Connection": "keep-alive",
#     "Cache-Control": "max-age=0",
#     "Upgrade-Insecure-Requests": "1",
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
#     # "Referer": "https://blog.csdn.net/qq_41782425/article/details/84934224",
#     # "Accept-Encoding": "gzip, deflate, br",
#     "Accept-Language": "zh-CN,zh;q=0.9",
#     "Cookie": "your cookie"
# }

# proxy = {
#     'HTTPS': '125.126.203.37:9999'
# }
# ip ='125.126.203.37:9999'
# html_response = requests.get('http://2019.ip138.com/ic.asp', proxies={'HTTPS': ip})
# with open('zip.txt', 'wb') as file:
#     file.write(html_response.content)



