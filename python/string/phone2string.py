#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-02-01 10:50:38
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : translate phone number to simple offset string

import hashlib

phone_number = "15321905912"

def auto_trans(src_str):
    for x in range(26):
        trans_table = str.maketrans('9876543210', 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'[x:x+10])
        print(src_str.translate(trans_table), chr(x + 97))

auto_trans(phone_number)

trans_tb = str.maketrans('rstuvwxyza', '9876543210')
#print("zvxyzravrzv".translate(trans_tb))


print(hashlib.md5(phone_number.encode(encoding='UTF-8')).hexdigest())

#662c0b61467eda7011714a70f59a8b67
#662c0b61467eda7011714a70f59a8b67