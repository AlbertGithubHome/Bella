#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-10-15 14:54:55
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : generate a tail slice from source file

import os

def tailslice(file_name, data_size= 1024):
    output_file, ext = os.path.splitext(file_name)
    with open(file_name, 'rb') as rfile:
        rfile.seek(-data_size, 2)
        with open('{0}_tail{1}'.format(output_file, ext), 'wb') as wfile:
            wfile.write(rfile.read())


if __name__ == '__main__':
    tailslice('GameDebug.log')