#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2020-7-1 22:49:35
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : 自动浏览网站

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

class tianyan_visitor(object):
    def __init__(self, entry_url):
        self.blog_url = entry_url
        self.article_list = []
        self.max_proxy_count = 5
        self.proxy_queue = Queue()
        self.agentpool = agentpool()
        self.proxy_pool_list = [proxypool('https://www.xicidaili.com/nn/', self.max_proxy_count),
            proxypool('https://www.xicidaili.com/nn/', self.max_proxy_count),
            proxypool('https://www.xicidaili.com/nn/', self.max_proxy_count)]

    def looking_for_investment(self, cur_level, max_level, url_list):
        next_level_url_list = []
        with open('company_detail_info_' + str(cur_level) +'.txt', 'a+', encoding='UTF-8') as file:
            for url in url_list:
                headers = {'User-Agent': self.agentpool.get_random_user_agent()} #, 'Connection': 'keep-alive'}
                response = requests.get(url,  headers=headers)
                if response.status_code == 200:

                    dom = etree.HTML(response.text)
                    file.write(response.text)

                    info_list = []

                    val = dom.xpath('//*[@id="company_web_top"]/div[2]/div[3]/div[1]/h1/text()') # 公司名称
                    print(url_list, val)
                    #info_list.append(val[0])
                    #company_name = val[0]

                    val = dom.xpath('//*[@id="_container_baseInfo"]/table[1]/tbody/tr[1]/td[1]/div[1]/div[1]/div[2]/div[1]/a/text()') # 法定代表人
                    info_list.append(val[0])

                    val = dom.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[1]/td[2]/div/text()') # 注册资本
                    info_list.append(val[0])
                    val = dom.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[1]/td[4]/text()') # 实缴资本
                    info_list.append(val[0])
                    val = dom.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[2]/td[2]/div/text()') # 成立日期
                    info_list.append(val[0])
                    val = dom.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[2]/td[4]/text()') # 经营状态
                    info_list.append(val[0])
                    val = dom.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[3]/td[2]/text()') # 统一社会信用代码
                    info_list.append(val[0])
                    val = dom.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[3]/td[4]/text()') # 工商注册号
                    info_list.append(val[0])
                    val = dom.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[4]/td[2]/text()') # 纳税人识别号
                    info_list.append(val[0])
                    val = dom.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[4]/td[4]/text()') # 组织机构代码
                    info_list.append(val[0])
                    val = dom.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[5]/td[2]/text()') # 公司类型
                    info_list.append(val[0])
                    val = dom.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[5]/td[4]/text()') # 行业
                    info_list.append(val[0])
                    val = dom.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[6]/td[2]/text/text()') # 核准日期
                    info_list.append(val[0])
                    val = dom.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[6]/td[4]/text()') # 登记机关
                    info_list.append(val[0])
                    val = dom.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[7]/td[2]/span/text()') # 营业期限
                    info_list.append(val[0])
                    val = dom.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[7]/td[4]/text()') # 纳税人资质
                    info_list.append(val[0])
                    val = dom.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[10]/td[2]/text()') # 注册地址
                    info_list.append(val[0])
                    val = dom.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[11]/td[2]/span/text()') # 经营范围
                    info_list.append(val[0])

                    file.write('\t'.join(info_list) + '\n')

                    if cur_level == max_level:
                        continue

                    with open('company_invest_info_' + str(cur_level) +'.txt', 'a+', encoding='UTF-8') as outfile:
                        name_list = dom.xpath('//*[@id="_container_invest"]/div/table/tbody/tr/td[2]/table/tr[1]/td[2]/div/a/text()') # 被投资企业名称
                        rate_list = dom.xpath('//*[@id="_container_invest"]/div/table/tbody/tr/td[6]/span/text()') # 投资比例
                        next_level_url_list = dom.xpath('//*[@id="_container_invest"]/div/table/tbody/tr/td[2]/table/tr[1]/td[2]/div/a/@href') # 网址
                        for name, rate, new_url in zip(name_list, rate_list, next_level_url_list):
                            outfile.write('{0}\t{1}\t{2}\n'.format(name, rate, new_url))


        if cur_level < max_level:
            self.looking_for_investment(cur_level + 1, max_level, next_level_url_list)


    def checker(self, thread_name): # 迷惑
        print('[INFO] 启动线程 {0} ...'.format(thread_name))
        content = input()
        if content == 'Q' or content == 'q':
            self.running = False

    def producer(self, thread_name):
        print('[INFO] 启动线程 {0} ...'.format(thread_name))

        if not self.article_list:
            print('[INFO] 没有文章需要访问，退出线程 {0} ...'.format(thread_name))
            return

        while self.running:
            while self.proxy_queue.qsize() < self.max_proxy_count:
                proxy_pool = random.choice(self.proxy_pool_list)
                proxy_list = proxy_pool.get_proxy_list()
                if not proxy_list:
                    print('[WARN] 尝试从 {0} 获取代理失败 ...'.format(proxy_pool.get_proxy_info_page()))
                    continue

                for proxy_item in proxy_list:
                    self.proxy_queue.put(proxy_item)
            else:
                print('[INFO] 当前代理池超过{0}，正等待消耗'.format(self.max_proxy_count))
                print('[INFO] 线程 {0} 沉睡 {1} 秒'.format(thread_name, 8))
                time.sleep(8)
        print('[INFO] 线程 {0} 退出 ...'.format(thread_name))

    def consumer(self, thread_name):
        print('[INFO] 启动线程 {0} ...'.format(thread_name))

        if not self.article_list:
            print('[INFO] 没有文章需要访问，退出线程 {0} ...'.format(thread_name))
            return
        print("[INFO] 开始等待准备代理，静默60秒")
        time.sleep(60)

        while self.running:
            while not self.proxy_queue.empty():
                proxies = self.proxy_queue.get()
                print("[INFO] 当前使用代理 {0} ...".format(proxies))
                article_url = random.choice(self.article_list)

                try:
                    headers = {'User-Agent': self.agentpool.get_random_user_agent()}
                    response = requests.get(article_url,  headers=headers, proxies=proxies, timeout=10)
                    if response.status_code == 200:
                        print("[INFO] 代理访问 {0} 成功!".format(article_url))
                        time.sleep(2)
                    else:
                        print("[WARN] 代理出现问题，静默4秒")
                        time.sleep(4)
                except Exception as e:
                    print("[ERRO] 代理访问出现错误 {0} 静默10秒".format(e))
                    time.sleep(10)
            else:
                try:
                    print("[WARN] 代理为空，放弃代理，直接访问CSDN，静默5秒")
                    for x in range(5):
                        article_url = random.choice(self.article_list)
                        headers = {'User-Agent': self.agentpool.get_random_user_agent()}
                        response = requests.get(article_url,  headers=headers, timeout=5)
                        if response.status_code == 200:
                            print("[INFO] 直接访问 {0} 成功!".format(article_url))
                            time.sleep(random.uniform(3.14, 6.18))
                except Exception as e:
                    print("[ERRO] 直接访问出现错误 {0} 静默5秒".format(e))
                finally:
                    time.sleep(5)
        print('[INFO] 线程 {0} 退出 ...'.format(thread_name))

    def run(self):
        self.looking_for_investment(1, 3, [self.blog_url])
        #self.running = True
        #Thread(target=self.checker, args=("checker",)).start()
        #Thread(target=self.producer, args=("producer",)).start()
        #Thread(target=self.consumer, args=("consumer",)).start()

if __name__ == '__main__':
    #auto_visitor = tianyan_visitor('https://www.tianyancha.com/company/13965639')
    #auto_visitor = tianyan_visitor('https://www.tianyancha.com/company/13966661')
    auto_visitor = tianyan_visitor('https://www.tianyancha.com/company/2894458295')
    auto_visitor.run()