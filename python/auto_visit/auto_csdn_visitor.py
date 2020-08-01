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
from selenium import webdriver

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
        self.use_selenium = False

    def parse_commands(self):
        self.log_file = 'logs/csdn_{0}.log'.format(time.strftime("%Y_%m_%d_%H%M%S", time.localtime()))

        if self.use_selenium:
            self.browser = webdriver.Firefox()

    def write_log(self, content):
        with open(self.log_file, 'a+', encoding='UTF-8') as file:
            file.write('[{0}]{1}\n'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), content))
        print(content)

    def get_request_header(self):
        return {'User-Agent': self.agentpool.get_random_user_agent(),
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
                'Accept-Encoding': 'gzip, deflate, br',
                #'Referer': 'https://blog.csdn.net/albertsh',
                'Connection': 'keep-alive',
                #'Cookie': 'uuid_tt_dd=10_30249464780-1582439878423-153400; dc_session_id=10_1582439878423.177641; UserName=weixin_41142820; UserInfo=9df529a9dd33454482a5c2ae179f9536; UserToken=9df529a9dd33454482a5c2ae179f9536; UserNick=AlbertS; AU=0C3; UN=shihengzhen101; BT=1582449168049; p_uid=U100000; __yadk_uid=q8v6OQ3c4n9H4SYvaAgCPuplvZ7HFqrn; Hm_lvt_3999cb4c6bca41993e741b74e1f08ef3=1591510544; Hm_up_3999cb4c6bca41993e741b74e1f08ef3=%7B%22islogin%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isonline%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isvip%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22uid_%22%3A%7B%22value%22%3A%22shihengzhen101%22%2C%22scope%22%3A1%7D%7D; Hm_ct_3999cb4c6bca41993e741b74e1f08ef3=5744*1*shihengzhen101!6525*1*10_30249464780-1582439878423-153400; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1591510544; searchHistoryArray=%255B%2522%25E5%258D%2597%25E5%25A2%2599%2522%252C%2522%25E4%25BD%25A0%25E5%25B1%2585%25E7%2584%25B6%25E8%25BF%2598%25E5%258E%25BB%25E6%259C%258D%25E5%258A%25A1%25E5%2599%25A8%25E4%25B8%258A%25E6%258D%259E%25E6%2597%25A5%25E5%25BF%2597%2522%255D; announcement=%257B%2522isLogin%2522%253Atrue%252C%2522announcementUrl%2522%253A%2522https%253A%252F%252Flive.csdn.net%252Froom%252Fcompanyzh%252F5o1Kf1RQ%253Futm_source%253D1593515841%2522%252C%2522announcementCount%2522%253A0%257D; dc_sid=fcc9fdd50534e9f672a9c8df1412f52e; TY_SESSION_ID=9389fe13-968a-4bd0-aaa9-16a18639b65c; c_first_ref=www.baidu.com; c_first_page=https%3A//blog.csdn.net/qq_42873554/article/details/106604859; c_utm_source=itdadao; c_utm_medium=distribute.pc_feed.none-task-blog-alirecmd-4.nonecase; dc_tos=qdptw5; c_ref=https%3A//blog.csdn.net/weixin_41142820; c_segment=8',
                'Upgrade-Insecure-Requests': '1',
                'Cache-Control': 'max-age=0',
                'TE': 'Trailers'
                }

    def get(self, url, sleep_pair=[0.1, 0.2], **kw):
        headers = self.get_request_header()

        if self.use_selenium:
            response = browser.get(url)
        else:
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
                    response = self.get(article_url, [10.21, 64.0], proxies=proxies, timeout=10)
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

        if self.use_selenium:
            self.browser.quit()

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