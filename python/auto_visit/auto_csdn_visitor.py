#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2020-05-24 21:42:35
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : 自动浏览CSDN网站文章

import os
import sys
import time
import random
import requests
from lxml import etree
from queue import Queue
from threading import Thread

sys.path.append(r"D:/data//maingit/Bella/python/tools/network")
from agentpool import agentpool
from proxypool import proxypool

class csdn_blog_visitor(object):
    def __init__(self, entry_url):
        self.blog_url = entry_url
        self.article_list = []
        self.proxy_queue = Queue()
        self.agentpool = agentpool()
        self.proxypool = proxypool()

    def retrieve_article_list(self):
        artcle_count = 0;
        with open('csdn_blog_article_list.txt', 'w', encoding='UTF-8') as file:
            for i in range(1, 10):
                headers = {'User-Agent': self.agentpool.get_random_user_agent(), 'Connection': 'keep-alive'}
                response = requests.get(self.blog_url + '/article/list/' + str(i),  headers=headers)
                if response.status_code == 200:
                    dom = etree.HTML(response.text)
                    article_url_list = dom.xpath('//*[@id="mainBox"]/main/div[2]/div[*]/h4/a/@href')
                    atticle_pv_list = dom.xpath('//*[@id="mainBox"]/main/div[2]/div[*]/div[1]/p/span[2]/text()')
                    # 文章查找完毕
                    if not article_url_list:
                        break
                    # 记录查找到的文章
                    for article_url, article_pv in zip(article_url_list, atticle_pv_list):
                        # 手动滑稽
                        file_path, file_name = os.path.split(article_url)
                        article_url = self.blog_url + '/article/details/' + file_name
                        # 内存记录并写入文件
                        self.article_list.append(article_url)
                        file.write('{0}\t{1}\n'.format(article_url, article_pv))
                        artcle_count += 1
        print('[INFO] 当前账号总共查找到 {0} 篇文章'.format(artcle_count))

    def producer(self, thread_name):
        print('[INFO] 启动线程 {0} ...'.format(thread_name))

        if not self.article_list:
            print('[INFO] 没有文章需要访问，退出线程 {0} ...'.format(thread_name))
            return

        while True:
            while self.proxy_queue.qsize() < 50:
                proxy_list = self.proxypool.get_proxy_list()
                for proxy_item in proxy_list:
                    self.proxy_queue.put(proxy_item)
            else:
                print("[WARN] 当前代理池超过50，正等待消耗")
                print('[WARN] 线程 {0} 沉睡 {1} 秒'.format(thread_name, 8))
                time.sleep(8)
        print('[INFO] 线程 {0} 退出 ...'.format(thread_name))

    def consumer(self, thread_name):
        print('[INFO] 启动线程 {0} ...'.format(thread_name))

        if not self.article_list:
            print('[INFO] 没有文章需要访问，退出线程 {0} ...'.format(thread_name))
            return
        print("[INFO] 开始等待准备代理，静默60秒")
        time.sleep(60)

        while True:
            while not self.proxy_queue.empty():
                proxies = self.proxy_queue.get()
                print("[INFO] 当前使用代理 {0} ...".format(proxies))
                article_url = random.choice(self.article_list)

                try:
                    headers = {'User-Agent': self.agentpool.get_random_user_agent(), 'Connection': 'keep-alive'}
                    response = requests.get(article_url,  headers=headers, proxies=proxies, timeout=10)
                    if response.status_code == 200:
                        print("[INFO] 代理访问 {0} 成功!".format(article_url))
                        time.sleep(2)
                    else:
                        print("[WARN] 代理出现问题，静默4秒")
                        time.sleep(4)
                except Exception as err:
                    print("[ERRO] CSDN访问出现问题，错误原因为 {0}，静默10秒".format(err))
                    time.sleep(10)
            else:
                print("[WARN] 代理为空，放弃代理，直接访问CSDN，静默5秒")
                for x in range(5):
                    article_url = random.choice(self.article_list)
                    headers = {'User-Agent': self.agentpool.get_random_user_agent(), 'Connection': 'keep-alive'}
                    response = requests.get(article_url,  headers=headers, timeout=2)
                    if response.status_code == 200:
                        print("[INFO] 直接访问 {0} 成功!".format(article_url))
                        time.sleep(2)
                time.sleep(5)
        print('[INFO] 线程 {0} 退出 ...'.format(thread_name))

    def run(self):
        self.retrieve_article_list()
        Thread(target=self.producer, args=("producer",)).start()
        Thread(target=self.consumer, args=("consumer",)).start()

if __name__ == '__main__':
    auto_visitor = csdn_blog_visitor('https://blog.csdn.net/albertsh')
    #auto_visitor.retrieve_article_list()
    auto_visitor.run()
    pass
    # proxy_queue = Queue()
    # proxy_queue.put(1)
    # proxy_queue.put([1,2])
    # print(proxy_queue.qsize())