#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2018-04-13 13:45:26
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : level 1 of python challenge
# 
# 思路：通过图片的提示K->M,O->Q,E->G可知，是需要将字母的ANSCII码加2，也就是向后移动两个字母，就此写出了custom_convert
#       然后使用图片下面的一堆乱码作为输入，输出结果只能看出部分含义，貌似标点、空格不需要翻译
#       在custom_convert基础上改进写出custom_convert2，发现断句正常，但是有些字母明显显示错误，比如tr{nsl{te应该是translate
#       分析后得知，这些出错的字母不是a就是b，所以应该是y和z向后移动两个字母时出的错误，就此写出了转换函数custom_convert3
#       custom_convert3转换后的结果提示：不用手动转换，可以借助函数string.maketrans，但是写代码时发现，这个函数的库名已经修改
#       于是改成了str.maketrans，并且封装了函数auto_trans(src_str)，在根据提示内容将url中的‘map’做为参数传入，得出下一关的url
#       map->ocr
#       
#       
# 备注：1. python challenge home page : http://www.pythonchallenge.com/
#       2. current level url : http://www.pythonchallenge.com/pc/def/map.html
#       3. next level url : http://www.pythonchallenge.com/pc/def/ocr.html

import functools
import string

source_str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

def custom_convert(x):
    return chr(ord(x) + 2)

def custom_convert2(x):
    if x.isalpha():
        return chr(ord(x) + 2)
    else:
        return x

def custom_convert3(x):
    if x.isalpha():
        return chr(ord('a') + (ord(x) - ord('a') + 2) % 26)
    else:
        return x

def merge_char(x, y):
    return x+y

def try_one(src_str):
    print(functools.reduce(merge_char, map(custom_convert, src_str)))

def try_two(src_str):
    print(functools.reduce(merge_char, map(custom_convert2, src_str)))

def try_three(src_str):
    print(functools.reduce(merge_char, map(custom_convert3, src_str)))

def auto_trans(src_str):
    trans_table = str.maketrans('abcdefghijklmnopqrstuvwxyz', 'cdefghijklmnopqrstuvwxyzab')
    print(src_str.translate(trans_table))


if __name__ == '__main__':
    #try_three(source_str)
    #try_three("map")
    auto_trans(source_str)
    auto_trans('map')


# 第一次尝试运行结果
'''
i"hope"you"didnt"tr{nsl{te"it"|y"h{nd0"th{ts"wh{t"computers"{re"for0"doing"it"in"|y"h{nd"is"inefficient"{nd"th{t)s"why"this"text"is"so"long0"using"string0m{ketr{ns*+"is"recommended0"now"{pply"on"the"url0
[Finished in 0.3s]
'''

# 第二次尝试运行结果
'''
i hope you didnt tr{nsl{te it |y h{nd. th{ts wh{t computers {re for. doing it in |y h{nd is inefficient {nd th{t's why this text is so long. using string.m{ketr{ns() is recommended. now {pply on the url.
[Finished in 0.2s]
'''

# 第三次尝试运行结果
'''
i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url.
[Finished in 0.5s]
'''

'''
i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url.
ocr
[Finished in 0.6s]
'''