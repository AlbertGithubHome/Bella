#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-10-14 16:46:14
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : split large log file to some parts

import os

DATA_LEN_PER_READ  = 1024 * 1024

def split_file_by_size(file_name, parts=3):
    file_size = os.path.getsize(file_name)
    per_file_size = file_size//parts
    file_size_list = []

    for x in range(parts-1):
        file_size_list.append(per_file_size)
    file_size_list.append(file_size-per_file_size*(parts-1))

    output_file, ext = os.path.splitext(file_name)
    with open(file_name, 'rb') as rfile:
        for n in range(parts):
            with open('{0}_part{1}{2}'.format(output_file, n+1, ext), 'wb') as wfile:
                read_size = 0
                while read_size < file_size_list[n]:
                    want_read = min(DATA_LEN_PER_READ, file_size_list[n] - read_size)
                    wfile.write(rfile.read(want_read))
                    read_size += want_read




def get_file_line_count(file_name):
    line_count = 0
    for index, line in enumerate(open(file_name, 'r')):
        line_count += 1
    return line_count

def split_file_by_line(file_name, parts=3):
    total_line = get_file_line_count(file_name)
    per_file_line = total_line//parts
    file_line_list = []

    for x in range(parts-1):
        file_line_list.append(per_file_line)
    file_line_list.append(total_line-per_file_line*(parts-1))

    output_file, ext = os.path.splitext(file_name)
    with open(file_name, 'rb') as rfile:
        for n in range(parts):
            with open('{0}_part{1}{2}'.format(output_file, n+1, ext), 'wb') as wfile:
                read_line = 0
                while read_line < file_line_list[n]:
                    wfile.write(rfile.readline())
                    read_line += 1


if __name__ == '__main__':
    # split_file_by_size('GameDebug.log')
    split_file_by_line('GameDebug.log')

