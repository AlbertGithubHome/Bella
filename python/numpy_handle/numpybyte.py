#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-3-25 16:39:38
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : numpy的字节大小端转换

import numpy as np
example_count = 0;


def aprint(v):
    global example_count
    example_count = example_count + 1
    print("---------------->{0}\n".format(example_count), v)

def main():
    a = np.array([1,  256,  8755], dtype = np.int16)
    aprint(a)
    aprint(list(map(hex, a)))
    aprint(a.byteswap(True))
    aprint(list(map(hex, a)))

if __name__ == '__main__':
    main()

'''
---------------->1
 [   1  256 8755]
---------------->2
 ['0x1', '0x100', '0x2233']
---------------->3
 [  256     1 13090]
---------------->4
 ['0x100', '0x1', '0x3322']
[Finished in 0.2s]
'''