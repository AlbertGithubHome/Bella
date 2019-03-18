#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-03-18 16:29:32
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : 测试numpy库的使用，生成对角矩阵

from numpy import *

def main():
    print(eye(5))

if __name__ == '__main__':
    main()


'''
[[1. 0. 0. 0. 0.]
 [0. 1. 0. 0. 0.]
 [0. 0. 1. 0. 0.]
 [0. 0. 0. 1. 0.]
 [0. 0. 0. 0. 1.]]
[Finished in 0.3s]
'''