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

sys.path.append(os.path.abspath("../tools/network"))
from agentpool import agentpool
from proxypool import proxypool

class csdn_blog_visitor(object):
    def __init__(self):
        self.blog_url = 'https://blog.csdn.net/albertsh'
        self.article_list = []
        self.visit_count = 0
        self.use_proxy = True
        self.max_proxy_count = 50
        self.proxy_queue = Queue()
        self.agentpool = agentpool()
        self.proxy_pool_list = [#proxypool('https://www.xicidaili.com/nn/', self.max_proxy_count),
            proxypool('localhost', self.max_proxy_count),
            proxypool('localhost', self.max_proxy_count)]

    def parse_commands(self):
        self.log_file = 'logs/csdn_{0}.log'.format(time.strftime("%Y_%m_%d_%H%M%S", time.localtime()))

    def write_log(self, content):
        with open(self.log_file, 'a+', encoding='UTF-8') as file:
            file.write('[{0}]{1}\n'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), content))
        print(content)

    def get_request_header(self):
        return {'User-Agent': self.agentpool.get_random_user_agent()} #, 'Connection': 'keep-alive'}

    def get(self, url, sleep_pair=[0.1, 0.2], **kw):
        headers = self.get_request_header()

        if 'proxies' in kw and 'timeout' in kw:
            response = requests.get(url, headers=headers, proxies=kw['proxies'], timeout=kw['timeout'])
        elif 'proxies' in kw:
            response = requests.get(url, headers=headers, proxies=kw['proxies'])
        elif 'timeout' in kw:
            response = requests.get(url, headers=headers, timeout=kw['timeout'])
        else:
            response = requests.get(url, headers=headers)

        sleep_time = random.uniform(sleep_pair[0], sleep_pair[1])
        if response.status_code == 200:
            self.visit_count += 1
            self.write_log("[INFO] [{0}] 访问 {1} 成功! 睡一会儿[{2}]".format(self.visit_count, url, round(sleep_time, 2)))

        time.sleep(sleep_time)

        return response;

    def collect_article_list(self):
        artcle_count = 0;
        self.write_log('[INFO] 开始收集文章列表'.format(artcle_count))
        with open('csdn_blog_article_list.txt', 'w', encoding='UTF-8') as file:
            for i in range(1, 10):
                response = self.get(self.blog_url + '/article/list/' + str(i), [1, 2])
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
                        prob = int(int(article_pv) / 500) + 1; # 非等概率，强者恒强

                        for x in range(prob):
                            self.article_list.append(article_url)

                        # 内存记录并写入文件
                        file.write('{0}\t{1}\t{2}\n'.format(article_url, article_pv, prob))
                        artcle_count += 1
        self.write_log('[INFO] 当前账号总共查找到 {0} 篇文章'.format(artcle_count))

    def checker(self, thread_name): # 迷惑
        self.write_log('[INFO] 启动线程 [{0}] ...'.format(thread_name))
        content = input()
        if content == 'Q' or content == 'q':
            self.running = False

    def producer(self, thread_name):
        self.write_log('[INFO] 启动线程 [{0}] ...'.format(thread_name))

        if not self.article_list:
            self.write_log('[INFO] 没有文章需要访问，退出线程 {0} ...'.format(thread_name))
            return

        while self.running:
            while self.proxy_queue.qsize() < self.max_proxy_count:
                proxy_pool = random.choice(self.proxy_pool_list)
                proxy_list = proxy_pool.get_proxy_list()
                if not proxy_list:
                    self.write_log('[WARN] 尝试从 {0} 获取代理失败 ...'.format(proxy_pool.get_proxy_info_page()))
                    continue

                for proxy_item in proxy_list:
                    self.proxy_queue.put(proxy_item)
            else:
                self.write_log('[INFO] 当前代理池个数 {0} 超过 {1}，正等待消耗'.format(
                    self.proxy_queue.qsize(), self.max_proxy_count))
                self.write_log('[INFO] 线程 [{0}] 沉睡 {1} 秒'.format(thread_name, 250))
                time.sleep(250)
        self.write_log('[INFO] 线程 [{0}] 退出 ...'.format(thread_name))

    def consumer(self, thread_name):
        self.write_log('[INFO] 启动线程 [{0}] ...'.format(thread_name))

        if not self.article_list:
            self.write_log('[INFO] 没有文章需要访问，退出线程 {0} ...'.format(thread_name))
            return

        if self.use_proxy:
            self.write_log("[INFO] 开始等待准备代理，静默60秒")
            time.sleep(60)

        while self.running:
            article_url = random.choice(self.article_list)
            pick_val = random.choice([1,2,3])
            if self.use_proxy and not self.proxy_queue.empty() and pick_val > 1:
                proxies = self.proxy_queue.get()
                self.write_log("[INFO] 当前使用代理 {0} ...".format(proxies))

                try:
                    response = self.get(article_url, [6.18, 13.14], proxies=proxies, timeout=10)
                    if response.status_code != 200:
                        self.write_log("[WARN] 代理出现问题，静默4秒")
                        time.sleep(4)
                except Exception as e:
                    self.write_log("[ERRO] 代理访问出现错误 {0} 静默10秒".format(e))
                    time.sleep(10)
            else:
                try:
                    self.write_log("[WARN] 代理为空，放弃代理，直接访问CSDN")
                    self.get(article_url, [10.21, 52.0], timeout=5)
                except Exception as e:
                    self.write_log("[ERRO] 直接访问出现错误 {0} 静默5秒".format(e))
                finally:
                    time.sleep(5)
        self.write_log('[INFO] 线程 [{0}] 退出 ...'.format(thread_name))

    def run(self):
        self.collect_article_list()
        self.running = True
        Thread(target=self.checker, args=("checker",)).start()
        Thread(target=self.producer, args=("producer",)).start()
        Thread(target=self.consumer, args=("consumer",)).start()

if __name__ == '__main__':
    auto_visitor = csdn_blog_visitor()
    auto_visitor.parse_commands()
    auto_visitor.run()