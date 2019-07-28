#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-7-28 11:57:02
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : random visit url of list

import time
import random
import toolbox
import requests
import datetime
import collect_articlelist

def random_visit(count, url_list):
    try:
        for x in range(0,count):
            visit_url = random.choice(url_list)
            head = {'User-Agent': toolbox.get_random_user_agent(), 'Connection': 'keep-alive'}
            requests.get(visit_url, headers=head)
            print("curtime = {0}, visit_url={1}".format(
                datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), visit_url))
            time.sleep(random.uniform(3.14, 6.18))
    except:
        print("try error")


def proxy_visit():
    try:
        visit_url = 'https://blog.csdn.net/albertsh/article/details/73512880'
        head = {'User-Agent': toolbox.get_random_user_agent(), 'Connection': 'keep-alive'}
        proxy_ip_port = toolbox.get_random_proxy()
        proxy_data = {'http': proxy_ip_port, 'https': proxy_ip_port}

        print("curtime = {0}, proxy= {1}, visit_url={2}".format(
            datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), proxy_ip_port, visit_url))
        
        requests.get(visit_url, headers=head, proxies=proxy_data)
        print("visit success")
    except:
        print("try error")



if __name__ == '__main__':
    proxy_visit()
    #random_visit(10, collect_articlelist.get_aticle_list())
    #print(collect_articlelist.get_aticle_list())
