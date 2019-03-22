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

import time
import requests
import re
import pickle
import os

# python challenge base class begin
# ---------------------------------->
class ChallengeMachine(object):
    def __init__(self, level, name, passwd, url):
        self.__level = level
        self.__name = name
        self.__passwd = passwd
        self.__url = url
        self.__home_page = 'http://www.pythonchallenge.com/'

    def run(self, re_download=False):
        start_time = time.time()
        print('level {0}: {1}'.format(self.get_level(), self.get_level_url()))
        if re_download:
            download_resource = getattr(self, 'download_resource')   # 获取子类的方法
            download_resource()
        action = getattr(self, 'action')
        next_key = action()
        print('next level key: {0}'.format(next_key))
        print('cost time: {0}s\n'.format(time.time() - start_time))

    def get_home_url(self):
        return self.__home_page

    def get_level_url(self):
        return self.__home_page + self.__url

    def get_level(self):
        return self.__level

    def get_resource_dir(self):
        dir_name = str(self.__level)
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
        return dir_name + '/'

    def download_resource(self):
        print("base download_resource")

    def action(self):
        print("base action")



# python challenge base class end
# ----------------------------------<



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


class CM3(ChallengeMachine):
    def action(self):
        html_content = requests.get(self.get_level_url()).content.decode('utf8')
        start_index = html_content.find('<!--')
        code_content = html_content[start_index:]
        return ''.join(re.findall(r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', code_content))


class CM4(ChallengeMachine):
    def action(self):
        nothing_value = '12345';
        try_count = 1
        while try_count < 400:
            html_content = requests.get(self.get_level_url() + '?nothing=' + nothing_value).content.decode('utf8')
            nothing_value = ''.join(re.findall(r'(\d+)', html_content))
            if len(nothing_value) == 0 and 'html' in html_content:
                return html_content
            try_count = try_count + 1
            print(nothing_value)
            time.sleep(0.3)


class CM5(ChallengeMachine):
    def download_resource(self):
        file_data = requests.get(self.get_home_url() + 'pc/def/banner.p').content
        data = pickle.loads(file_data)
        with open(self.get_resource_dir() + 'pic.txt', 'w') as file:
            file.write('\n'.join([''.join([p[0] * p[1] for p in row]) for row in data]))

    def action(self):
        return 'channel'


class CM6(ChallengeMachine):
    def download_resource(self):
        file_data = requests.get(self.get_home_url() + 'pc/def/channel.zip').content
        with open(self.get_resource_dir() +'channel.zip', 'wb') as file:
            file.write(file_data)

    def action(self):
        return 'channel'


def main():
    #CM0(0, None, None, 'pc/def/0.html').run()
    #CM1(1, None, None, 'pc/def/274877906944.html').run()
    #CM2(2, None, None, 'pc/def/ocr.html').run()
    #CM3(3, None, None, 'pc/def/equality.html').run()
    #CM4(4, None, None, 'pc/def/linkedlist.php').run()
    CM5(5, None, None, 'pc/def/peak.html').run()
    CM6(6, None, None, 'pc/def/channel.html').run(True)




def test():
    letter_list = re.findall(r'(\d+)', 'ahfakdsds')
    print(letter_list)
    print(len(letter_list))
    print(len(''.join(letter_list)))

    return False

if __name__ == '__main__': main()

