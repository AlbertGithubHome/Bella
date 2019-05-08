#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-04-12 18:07:57
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : 尝试访问一个网站
#

import requests

target_url = 'https://blog.csdn.net/albertsh/article/details/52231311'

def main():
    html_content = requests.get(target_url).content
    #print(html_content)
    with open('request.html', 'wb') as file:
        file.write(html_content)


if __name__ == '__main__':
    main()

