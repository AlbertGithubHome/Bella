#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#a solution for palindrome game
#example 仙人似美娟 * 我 = 娟美似人仙
#result: 21978 * 4

__author__ = 'AlbertS'

def is_contain_same(curItem):
    dtable = {}
    for x in curItem:
        if x in dtable:
            return True
        else:
            dtable[x] = 1
    return False

def find_palindrome():
    for x in range(10000,100000):
        curItem = str(x)
        revItem = curItem[::-1]
        for me in range(1,10):
            if is_contain_same(curItem + str(me)):
                continue
            elif x * me == int(revItem):
                print("ret:", x, me)

if __name__ == "__main__":
    find_palindrome()

#公式： 仙人似美娟 * 我 = 娟美似人仙
#含义： 善解人意的娟娟 在我的眼里 就像仙女一样美丽

