#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-3-19 14:19:04
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : ndarray运算时的广播

import numpy as np
example_count = 0;


def aprint(v):
    global example_count
    example_count = example_count + 1
    print("---------------->{0}\n".format(example_count), v)


def main():
    a = np.array([1,2,3,4])
    b = np.array([10,20,30,40])
    c = a * b
    aprint(c)

    a = np.array([[ 0, 0, 0],
           [10,10,10],
           [20,20,20],
           [30,30,30]])
    b = np.array([1,2,3])
    aprint(a + b)


if __name__ == '__main__':
    main()

'''
---------------->1
 [ 10  40  90 160]
---------------->2
 [[ 1  2  3]
 [11 12 13]
 [21 22 23]
 [31 32 33]]
[Finished in 0.3s]
'''