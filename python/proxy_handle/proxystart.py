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

import agents
import requests

print(agents.get_user_agents())
# html_response = requests.get('http://2019.ip138.com/ic.asp') #('http://www.ip138.com/')
# with open('ip.txt', 'wb') as file:
#     file.write(html_response.content)

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
}
#  定义代理的字典
# proxies = {
#     #"http": "http://121.228.8.93:8118"
#     "http://120.68.158.212:9000"
# }
# proxies={'http':'120.68.158.212:9000'}

proxies = {
  "http": "http://10.10.1.10:3128",
  "https": "http://10.10.1.10:1080",
}

#requests.get("http://example.org", proxies=proxies)

# 使用代理给服务器发送请求
html_response = requests.get('http://2019.ip138.com/ic.asp', proxies=proxies, headers=headers)
with open('ip.txt', 'wb') as file:
    file.write(html_response.content)





