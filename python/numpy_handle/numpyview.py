#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-3-25 16:41:31
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : numpy的副本和视图

import numpy as np
example_count = 0;


def aprint(v):
    global example_count
    example_count = example_count + 1
    print("---------------->{0}\n".format(example_count), v)

def main():
    a = np.arange(6)
    aprint(a)
    b = a
    aprint(b)
    b.reshape(3, 2) # reshape不改变
    aprint(a)
    b.shape = 3, 2 # .shape就改变了
    aprint(a)

    a = np.arange(6)
    aprint(a)
    b = a.view()
    aprint(id(a))
    aprint(id(b))
    b.shape = 3, 2
    aprint(b)
    aprint(a) # 修改b后a不改变

    b = a[3:]
    b[0] = 100
    aprint(a)

    a = np.arange(6)
    aprint(a)
    b = a.copy()
    b.shape = 3, 2 # .shape改变不影响copy前的数组
    aprint(a)



if __name__ == '__main__':
    main()

'''
---------------->1
 [0 1 2 3 4 5]
---------------->2
 [0 1 2 3 4 5]
---------------->3
 [0 1 2 3 4 5]
---------------->4
 [[0 1]
 [2 3]
 [4 5]]
---------------->5
 [0 1 2 3 4 5]
---------------->6
 1694176633200
---------------->7
 1694176633920
---------------->8
 [[0 1]
 [2 3]
 [4 5]]
---------------->9
 [0 1 2 3 4 5]
---------------->10
 [  0   1   2 100   4   5]
---------------->11
 [0 1 2 3 4 5]
---------------->12
 [0 1 2 3 4 5]
[Finished in 0.2s]
'''