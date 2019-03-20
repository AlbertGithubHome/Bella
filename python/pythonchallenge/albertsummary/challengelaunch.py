#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-03-19 17:29:31
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : 将Python challenge所有关卡总结在一起
#
# 思路：参照之前的思路尽可能优化，减少实现的代码量

import requests


class ChallengeMachine(object):
    def __init__(self, level, name, passwd, url):
        self.__level = level
        self.__name = name
        self.__passwd = passwd
        self.__url = url
        self.__home_page = 'http://www.pythonchallenge.com/'


    def run(self, re_download=False):
        print('level {0}: {1}'.format(self.__level, self.__home_page + self.__url))
        if re_download:
            download_resource = getattr(self, 'download_resource')   # 获取子类的方法
            download_resource()
        action = getattr(self, 'action')
        next_key =action()
        print('next level key: {0}\n'.format(next_key))

    def get_level_url(self):
        return self.__home_page + self.__url

    def download_resource(self):
        print("base download_resource")

    def action(self):
        print("base action")


class CM0(ChallengeMachine):
    def action(self):
        return 2**38


class CM1(ChallengeMachine):
    def action(self):
        trans_table = str.maketrans('abcdefghijklmnopqrstuvwxyz', 'cdefghijklmnopqrstuvwxyzab')
        return 'map'.translate(trans_table)


class CM2(ChallengeMachine):
    def action(self):
        html_content = requests.get(self.get_level_url()).content.decode('utf8')
        start_index = html_content.find('$@_$^__#)')
        code_content = html_content[start_index:]
        return ''.join([x for x in code_content if x.isalpha()])


def main():
    CM0(0, None, None, 'pc/def/0.html').run()
    CM1(1, None, None, 'pc/def/274877906944.html').run()
    CM2(2, None, None, 'pc/def/ocr.html').run()

if __name__ == '__main__': main()

