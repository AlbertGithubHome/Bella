#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-3-22 11:24:02
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : numpy的算术运算

import numpy as np
example_count = 0;


def aprint(v):
    global example_count
    example_count = example_count + 1
    print("---------------->{0}\n".format(example_count), v)


def main():
    a = np.array([0, 10, 20])
    b = np.arange(1, 10).reshape(3, 3)
    c = np.array([2, 3, 4])
    aprint(a)
    aprint(b)
    aprint(a + b)
    aprint(np.add(a, b))
    aprint(np.subtract(a, b))
    aprint(np.multiply(a, b))
    aprint(np.divide(a, b))

    aprint(np.reciprocal(b * 1.0))
    aprint(np.power(a, 3))
    aprint(np.mod(a, b))
    #aprint(np.mod(c, a))



if __name__ == '__main__':
    main()

'''


[Finished in 0.3s]
'''