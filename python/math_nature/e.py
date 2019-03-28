#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-03-28 13:45:32
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : 实现一个近似求解e的的方法
#
# 思路：利用乘方近似求解e的极限值

def calc_e(n):
    return (1 + 1 / n) ** n

if __name__ == '__main__':
    fake_e = calc_e(1000000)
    print(fake_e)

