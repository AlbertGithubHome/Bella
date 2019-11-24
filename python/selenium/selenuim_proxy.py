#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-11-23 23:09:58
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : use selenium to visit web with proxy

import time
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

profile = FirefoxProfile()
# 激活手动代理配置（对应着在 profile（配置文件）中设置首选项）
profile.set_preference("network.proxy.type", 1)
# ip及其端口号配置为 http 协议代理
profile.set_preference("network.proxy.http", "49.51.193.128")
profile.set_preference("network.proxy.http_port", 1080)

# 所有协议共用一种 ip 及端口，如果单独配置，不必设置该项，因为其默认为 False
profile.set_preference("network.proxy.share_proxy_settings", True)

# 默认本地地址（localhost）不使用代理，如果有些域名在访问时不想使用代理可以使用类似下面的参数设置
# profile.set_preference("network.proxy.no_proxies_on", "localhost")

# 以代理方式启动 firefox
browser  = webdriver.Firefox(profile)
browser.delete_all_cookies()
browser.maximize_window()
browser.get('http://httpbin.org/get')
time.sleep(5)
browser.quit()