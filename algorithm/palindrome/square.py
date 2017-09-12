#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#a solution for palindrome game
#example (he) ^ 2 = she
#result: 25 ^ 2 = 625

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
    for x in range(10, 100):
        curItem = str(x)
        curRet  = str(x * x)
        posRet = curRet[-2:]
        if is_contain_same(curItem) or is_contain_same(curRet):
            continue
        elif curItem == posRet:
            print("ret:", curItem, curRet)

if __name__ == "__main__":
    find_palindrome()




