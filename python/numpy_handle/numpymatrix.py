#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-3-25 17:06:41
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : numpy的矩阵库

import numpy as np
import numpy.matlib
example_count = 0;


def aprint(v):
    global example_count
    example_count = example_count + 1
    print("---------------->{0}\n".format(example_count), v)

def main():
    aprint(np.matlib.empty((2, 2)))

    aprint(np.matlib.zeros((2, 2)))

    aprint(np.matlib.ones((2, 3)))

    aprint(np.matlib.eye(3, 4, 0))

    aprint(np.matlib.identity(5))

    a = np.matrix('1,2;3,4')
    aprint(a)
    b = np.asarray(a);
    aprint(b)
    c = np.asmatrix(b)
    aprint(c)



if __name__ == '__main__':
    main()

'''
---------------->1
 [[9.90263869e+067 8.01304531e+262]
 [2.60799828e-310 1.91158065e+214]]
---------------->2
 [[0. 0.]
 [0. 0.]]
---------------->3
 [[1. 1. 1.]
 [1. 1. 1.]]
---------------->4
 [[1. 0. 0. 0.]
 [0. 1. 0. 0.]
 [0. 0. 1. 0.]]
---------------->5
 [[1. 0. 0. 0. 0.]
 [0. 1. 0. 0. 0.]
 [0. 0. 1. 0. 0.]
 [0. 0. 0. 1. 0.]
 [0. 0. 0. 0. 1.]]
---------------->6
 [[1 2]
 [3 4]]
---------------->7
 [[1 2]
 [3 4]]
---------------->8
 [[1 2]
 [3 4]]
[Finished in 0.2s]

'''