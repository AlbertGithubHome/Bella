#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2020-08-27 23:23:45
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : 练习时间转化函数


import time

val = time.time()
print(val, type(val))

'''输出结果
1598769108.8337526
'''

import time

val = time.struct_time([2020, 8, 30, 14, 45, 30, 6, 243, 0])
print(val, type(val))
'''输出结果
time.struct_time(tm_year=2020, tm_mon=8, tm_mday=30, tm_hour=14,
    tm_min=45, tm_sec=30, tm_wday=6, tm_yday=243, tm_isdst=0)
'''


import time

val = '2019-08-30 15:04:00'
print(val, type(val))
'''输出结果
2019-08-30 15:04:00 <class 'str'>
'''

t = time.time()
print(t)

l = time.localtime(t)
print(l)

s = time.strftime("%Y-%m-%d %X", l)
print(s)

print(time.asctime(time.localtime()))
print(time.ctime(time.time()))

print("===")

import time

# 生成时间戳
t = time.time()
print(t, type(t))
'''
1598775821.840567 <class 'float'>
'''

# 生成时间结构对象(本地时间)
l = time.localtime()
print(l, type(l))
'''
time.struct_time(tm_year=2020, tm_mon=8, tm_mday=30, tm_hour=16, tm_min=23,
 tm_sec=41, tm_wday=6, tm_yday=243, tm_isdst=0) <class 'time.struct_time'>
'''

# 时间戳 -> 时间结构对象(本地时间)
l = time.localtime(t)
print(l, type(l))
'''
time.struct_time(tm_year=2020, tm_mon=8, tm_mday=30, tm_hour=16, tm_min=23,
 tm_sec=41, tm_wday=6, tm_yday=243, tm_isdst=0) <class 'time.struct_time'>
'''

# 生成时间结构对象(格林威治时间)
g = time.gmtime()
print(g, type(g))
'''
time.struct_time(tm_year=2020, tm_mon=8, tm_mday=30, tm_hour=8, tm_min=23,
 tm_sec=41, tm_wday=6, tm_yday=243, tm_isdst=0) <class 'time.struct_time'>
'''

# 时间戳 -> 时间结构对象(格林威治时间)
g = time.gmtime(t)
print(g, type(g))
'''
time.struct_time(tm_year=2020, tm_mon=8, tm_mday=30, tm_hour=8, tm_min=23,
 tm_sec=41, tm_wday=6, tm_yday=243, tm_isdst=0) <class 'time.struct_time'>
'''


# 生成时间字符串
s = time.strftime("%Y-%m-%d %X")
print(s, type(s))
'''
2020-08-30 16:23:41 <class 'str'>
'''

# 时间结构对象 -> 时间字符串
s = time.strftime("%Y-%m-%d %X",time.localtime())
print(s, type(s))
'''
2020-08-30 16:23:41 <class 'str'>
'''

'================================================================='

# 定义时间字符串
s = '2022-02-18 09:30:00'

# 时间字符串 -> 时间结构对象
l = time.strptime(s, '%Y-%m-%d %X')
print(l, type(l))
'''
time.struct_time(tm_year=2022, tm_mon=2, tm_mday=18, tm_hour=9, tm_min=30,
 tm_sec=0, tm_wday=4, tm_yday=49, tm_isdst=-1) <class 'time.struct_time'>
'''

# 时间结构对象 -> 时间戳
t = time.mktime(l)
print(t, type(t))
'''
1645147800.0 <class 'float'>
'''

'================================================================='

# 生成固定格式(%a %b %d %H:%M:%S %Y)时间字符串
s = time.asctime(time.localtime())
print(s, type(s))
'''
Sun Aug 30 16:23:41 2020 <class 'str'>
'''


s = time.ctime(time.time())
print(s, type(s))
'''
Sun Aug 30 16:23:41 2020 <class 'str'>
'''

'================================================================='

s = time.strftime("%Y%m%d_%H%M%S",time.localtime())
print(s)