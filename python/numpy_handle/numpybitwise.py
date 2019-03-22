#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-3-21 15:59:49
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : numpy的位运算

import numpy as np
example_count = 0;


def aprint(v):
    global example_count
    example_count = example_count + 1
    print("---------------->{0}\n".format(example_count), v)


def main():
    a = np.arange(8)
    b = np.array([1, 3, 4, 3, 5, 6, 7, 8])
    aprint(np.bitwise_and(a, b))
    aprint(np.bitwise_or(a, b))
    aprint(np.invert(a))
    aprint(np.left_shift(a, 2))
    aprint(np.right_shift(a, 2))

    aprint(np.left_shift(10, 2))
    aprint(np.right_shift(10, 2))

    aprint(bin(1))
    aprint(bin(-1))
    aprint("{0:b}".format(1))
    aprint("{0:b}".format(-1))
    aprint(format(1543, 'b'))
    aprint(format(-1, 'b'))
    aprint(bin(np.invert(1)))
    print(bin(np.invert(2)))

    aprint(np.right_shift(-1, 10))
    aprint(np.right_shift(128, 1))
    aprint(np.right_shift(-2, 1))

    # 0 取反是 -1
    # 1 取反是 -2
    # 2 取反是 -3
    # 3 取反是 -4
    # ...
    # 127 取反是 -128

if __name__ == '__main__':
    main()

'''

[Finished in 0.3s]

'''