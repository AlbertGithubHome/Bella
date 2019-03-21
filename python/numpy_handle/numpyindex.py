#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-03-19 10:21:16
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : ndarray的各种索引

import numpy as np
example_count = 0;


def aprint(v):
    global example_count
    example_count = example_count + 1
    print("---------------->{0}\n".format(example_count), v)


def main():
    x = np.array([[1,  2],  [3,  4],  [5,  6]])
    y = x[[0,1,2],  [0,1,0]]
    aprint (y)

    y = x[[[0,1,2]],  [[0,1,0]]]
    aprint (y)

    y = x[[[0,1,2], [1, 0, 2]],  [[0,1,0], [1, 0, 0]]]
    aprint (y)

    y = x[x < 4]
    aprint (y)

    #y = x[[x < 4]]
    #aprint (y)

    x = np.arange(14)
    y = x[x < 5]
    aprint (y)

    x = np.array([1, 2, 3, 4, 5, np.nan, 7])
    y = x[~np.isnan(x)]
    aprint (y)

    x = np.arange(32).reshape((8,4))
    aprint(x[[-4,-3,-2,-5]])

    x = np.arange(32).reshape((8,4)) #对比下面的例子理解一下花式数组索引np.ix_
    aprint(x[np.ix_([1,5,7,2],[0,3,1,2])])

    x = np.arange(32).reshape((8,4))
    aprint(x[[1,5,7,2],[0,3,1,2]])


if __name__ == '__main__':
    main()

'''
---------------->1
 [1 4 5]
---------------->2
 [[1 4 5]]
---------------->3
 [[1 4 5]
 [4 1 5]]
---------------->4
 [1 2 3]
---------------->5
 [0 1 2 3 4]
---------------->6
 [1. 2. 3. 4. 5. 7.]
---------------->7
 [[16 17 18 19]
 [20 21 22 23]
 [24 25 26 27]
 [12 13 14 15]]
---------------->8
 [[ 4  7  5  6]
 [20 23 21 22]
 [28 31 29 30]
 [ 8 11  9 10]]
---------------->9
 [ 4 23 29 10]
[Finished in 0.3s]
'''