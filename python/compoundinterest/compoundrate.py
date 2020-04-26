#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2020-04-23 22:58:25
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : xxxx
#
# 思路：xxxx

X = 0.01
while X <= 0.05:
    A=5667.7
    C=X/12
    TOTAL= A
    for x in range(240-1):
        TOTAL = TOTAL * (1 + C)  + A;

    #print(TOTAL)
    X = X + 0.001

X = 0.01
while X <= 0.05:
    A=3143.5
    C=X/12
    TOTAL= A
    for x in range(360-1):
        TOTAL = TOTAL * (1 + C)  + A;

    #print(TOTAL)
    X = X + 0.001

X = 0.033
A=5667.7
C=X/12
TOTAL= A
for x in range(240-1):
    TOTAL = TOTAL * (1 + C)  + A;
    print(TOTAL)