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
                    user_proxy = random.choice(proxies_list)
                    target_url = random.choice(targer_urls)
                    print('try count = {0}, proxy = {1}, url = {2}'.format(try_count, user_proxy, target_url))
                    file.write('try count = {0}, fail count = {1}, proxy = {2}, url = {3}, agent = {4}\n'.format(try_count,
                        fail_count, user_proxy, target_url, user_agent))
                    html_response = requests.get(target_url, proxies={'http': user_proxy}, headers={'User-Agent': user_agent})
                    try_count += 1
                    with open("target.html", "wb") as page:
                        page.write(html_response.content)
                    time.sleep(random.uniform(1.1, 3.3))
                    pass
                except:
                    break
            fail_count += 1


if __name__ == '__main__':
    start_crawler()


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

