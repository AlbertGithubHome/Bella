#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2020-03-13 22:57:48
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : 将制定目录下文件按照文件修改日期排序，可用于查找错误时间的文件
#             比如把电脑时间往将来调了几天，改了文件，然后把时间恢复，每次都要重新编译
#             这时可以通过这个工具找到这些文件，再保存一下就好了

import os
import sys
import time

NORMALIZATION_PATH_LEN=64

def get_file_list(root_path='.', hidden_oldfile=False, reverse_sort=False):
    result_list = []
    now_time = time.time()
    for root, dir, files in os.walk(root_path):
        for file in files:
            full_path = os.path.join(root, file)
            mtime = os.stat(full_path).st_mtime
            if not hidden_oldfile or mtime > now_time:
                file_modify_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mtime))
                date_info = "{0} <=> {1}".format(file_modify_time, full_path)
                result_list.append(date_info)

    result_list.sort(reverse=reverse_sort)
    return result_list

def format_file_path(path_str):
    if len(path_str) <= NORMALIZATION_PATH_LEN:
        return path_str
    else:
        path_name,file_name=os.path.split(path_str);
        return path_name[0:NORMALIZATION_PATH_LEN-len(file_name)-10]+'...'+path_str[len(path_str)-len(file_name)-7:]


def start_list(root_path='.', hidden_oldfile=False, reverse_sort=False,format_path=False):
    for x in get_file_list(root_path,hidden_oldfile,reverse_sort):
        print(format_path and format_file_path(x) or x)

if __name__ == '__main__':
    start_list('D:\\data\\maingit\\encoding')