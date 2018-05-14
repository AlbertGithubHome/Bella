#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2018-05-14 19:42:05
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : level 10 of python challenge
# 
# 思路：这一关在页面上有"len(a[30]) = ?"这个提示，也就是要求a[30]的长度喽，那得先找到a[30]
#       打开网页源码有一个文件链接href="sequence.txt",点击进入发现数列a = [1, 11, 21, 1211, 111221, 
#       居然是一部分，那就是让我们自己推算了，按程序猿的世界来说a[0] = 1, a[1] = 11, a[2] = 21,可是
#       a[30]究竟是多少呢，查了一下这个数列，据说叫做"Look and Say"序列，也就是说后一个元素是对前一个元素的描述，
#       第2个数：是对第一个数的描述：1--->11-->1个1.
#       第3个数：是对第二个数的描述：11-->21-->2个1.
#       第4个数：是对第三个数的描述：21-->1211-->1个2，2个1.
#       ...
#       那么循环求出第31个数，也就是a[30]，那么这道题就解出来了，可是从前一个数推后一个数需要循环求解，写起来挺麻烦的
#       我们如果可以把数字顺序截成一些小段，每段中只包含一种数字就好了，比如12211，截成1、22、11，这样们就可以描述它们了
#       这里可以用正则表达式，利用Python对标准正则表达式扩展，其中有一种用法是命名组，写成r'((?P<word>\d)(?P=word)*)'
#       这个正则表达式的含义就是命名了一个组叫做word，这个组捕获一个数字，然后后续(?P=word)*表示有0到多个word组捕获的数字
#       也就是顺序找出所有连续相同的内容，最少为1个数字，这样就可以把内容分隔开了，第一个数字是1，然后循环30次得到结果5808
#       
# 
# 备注：1. python challenge home page : http://www.pythonchallenge.com/
#       2. current level url : http://www.pythonchallenge.com/pc/return/bull.html
#       3. next level url : http://www.pythonchallenge.com/pc/return/5808.html
#       4. username:huge password:file

import re
import functools

def main():
    asequence = '1'
    for x in range(0,30):
        asequence = functools.reduce(lambda x, y : x + y, map(lambda m:'%s%s'%(len(m[0]), m[1]), 
            re.findall(r'((?P<word>\d)(?P=word)*)', asequence)))
    print(len(asequence))


if __name__ == '__main__':
    main()



# 运行结果还是很快的
'''
5808
[Finished in 0.2s]
'''

