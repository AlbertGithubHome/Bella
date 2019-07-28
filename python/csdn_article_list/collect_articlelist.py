#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-7-28 10:12:39
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : acquire csdn article url list

import re
import time
import random
import toolbox
import requests
import datetime

main_url = 'https://blog.csdn.net/albertsh/article/list/'

def get_url_data(url):
    try:
        head = {'User-Agent': toolbox.get_random_user_agent(), 'Connection': 'keep-alive'}
        return requests.get(url, headers=head).text
    except:
        return ""


def extract_url(data):
    result_set = set()
    line_list = data.split('\n')
    for line in line_list:
        try:
            result = re.search('.*<a href="(https://blog.csdn.net/shihengzhen101/article/details/\d{1,10})" target="_blank">.*', line)
            if result:
                result_set.add(result.groups()[0])
        except:
            return result_set
    return result_set

def archive_aticle_list(save):
    result_set = set()
    try:
        for x in range(1,10):
            visit_url = main_url+str(x);
            print("curtime = {0}, visit_url={1}".format(
                datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), visit_url))
            page_set = extract_url(get_url_data(visit_url))
            result_set.update(page_set)
            time.sleep(random.uniform(3.14, 6.18))
    except:
        pass
    finally:
        result_num = len(result_set)
        if not save:
            print(result_set)
            print(result_num)
        else:
            count = 1
            with open('articlelist.txt', 'w') as file:
                for line in result_set:
                    file.write(count == result_num and line or line+'\n')
                    count +=1

def get_aticle_list(refresh=False):
    if refresh:
        archive_aticle_list(True)

    with open('articlelist.txt', 'r') as file:
        data = file.read();
        return data.split("\n")

if __name__ == '__main__':
    archive_aticle_list(True)
