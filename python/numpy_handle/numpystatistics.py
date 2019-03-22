#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-3-22 11:37:11
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : numpy的统计函数

import numpy as np
example_count = 0;


def aprint(v):
    global example_count
    example_count = example_count + 1
    print("---------------->{0}\n".format(example_count), v)

def test():
    user_name = 'a%';
    #user_name = "a\' or \'1\'=\'1"
    #user_name = "a' or '1'='1"
    print('SELECT password FROM admins WHERE username=\'%s\'' % user_name.replace('%', '%%'))

'''
    test'; INSERT INTO admins (username, password) VALUES ('test', '1');

'''

# username = 'a' and password = 'b';

# username = 'a' and password = 'b';

# ```sql
# username = 'a' or 1==1 -- and password = 'b';
# ```

def main():
    a = np.array([[3,7,5],[8,4,3],[2,4,9]])
    aprint(a)
    aprint(np.amin(a))  # 不加就是所有元素了
    aprint(np.amin(a, axis = 0))
    aprint(np.amin(a, axis = 1))

    aprint(np.amax(a))  # 不加就是所有元素了
    aprint(np.amax(a, axis = 0))
    aprint(np.amax(a, axis = 1))

    aprint(np.ptp(a))           # 最大最小值差
    aprint(np.ptp(a, axis = 0))
    aprint(np.ptp(a, axis = 1))

    aprint(np.percentile(a, 50)) #以50%作为分割线选出轴
    aprint(np.percentile(a, 50, 0))
    aprint(np.percentile(a, 50, 1))


    aprint(np.median(a))            # 中位数
    aprint(np.median(a, axis = 0))
    aprint(np.median(a, axis = 1))

    aprint(np.mean(a))              # 算术平均值
    aprint(np.mean(a, axis = 0))
    aprint(np.mean(a, axis = 1))

    b = np.array([1, 2, 3, 4])      # 加权平均值
    aprint(np.average(b))
    w = np.array([4, 3, 2, 1])
    aprint(np.average(b, weights = w))
    aprint(np.average(b, weights = w, returned = True))


    aprint(np.var([1,2,3,4]))        # 方差

    aprint(np.std([1,2,3,4]))        # 标准差



if __name__ == '__main__':
    main()

'''


[Finished in 0.3s]
'''