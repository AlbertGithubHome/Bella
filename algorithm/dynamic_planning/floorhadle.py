#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2018-08-25 12:37:13
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : handle floor 1x1 or 1x2 to area of 1xn

def handle_floor(n):
    if n <= 2:
        return n

    pre_val = 1;
    now_val = 2;
    for x in range(3, n + 1):
        tmp = now_val;
        now_val = now_val + pre_val;
        pre_val = tmp

    return now_val


# start to handle floor
if __name__ == '__main__':
    while(True):
        n = int(input("please input length num:"))
        result = handle_floor(n)
        print('result is {0}'.format(result))
