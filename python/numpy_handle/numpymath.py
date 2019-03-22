#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-3-22 10:57:40
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : numpy的数学运算

import numpy as np
example_count = 0;


def aprint(v):
    global example_count
    example_count = example_count + 1
    print("---------------->{0}\n".format(example_count), v)


def main():
    a = np.array([0, 30, 45, 60, 90])
    aprint(np.sin(a * np.pi / 180))
    aprint(np.cos(a * np.pi / 180))
    aprint(np.degrees(np.pi))
    aprint(np.radians(np.pi))
    aprint(np.radians(180))
    aprint(np.tan(np.radians(a)))

    aprint(np.degrees(np.arctan(1)))

    b = np.array([12.23, 54.3232, 54.89433, -4.4, -5.5])
    aprint(np.around(b))
    aprint(np.floor(b))
    aprint(np.ceil(b))



if __name__ == '__main__':
    main()

'''


[Finished in 0.3s]
'''