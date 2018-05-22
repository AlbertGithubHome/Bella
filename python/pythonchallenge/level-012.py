#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2018-05-17 19:35:27
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : level 12 of python challenge
# 
# 思路：这一关和上一关一样只有一张模糊的图，说实话一点不会，然后膜拜大神思路。
#       在源代码中发现图片的名字为evil1.jpg，进而查看evil2.jpg，然后查看evil3.jpg
#       发现evil2.jpg中的内容为not jpg .gfx，而evil3.jpg的内容为no more  evils
#       当前关卡中的标题为dealing evil，于是把evil2.jpg改为evil2.gfx发现是二进制文件
#       这应该就是需要处理的evil吧，于是下载下来，在根据本关开始时的那副图中扑克牌被分成了五堆
#       所以把这个二进制文件分成5份，分别存为图片，然后将图片上的字母连接起来，去掉划线的字母
#       得到最终的内容是disproportional，也就是下关的url
# 
# 备注：1. python challenge home page : http://www.pythonchallenge.com/
#       2. current level url : http://www.pythonchallenge.com/pc/return/evil.html
#       3. next level url : http://www.pythonchallenge.com/pc/return/disproportional.html
#       4. username:huge password:file
#       5. 做13关的时候发现有一条线索来自12关，查看图片evil4.jpg，也就是访问网址：
#           http://www.pythonchallenge.com/pc/return/evil4.jpg，得到一句话Bert is evil! go back!
#           注意必须用IE浏览器才能看到，火狐、google都看不到，这就是游戏所在，明明evil3.jpg的内容是
#           no more evils，结果在evil4.jpg中隐藏着真正的evil

from PIL import Image
import requests
import io

# image url
target_url = 'http://www.pythonchallenge.com/pc/return/evil2.gfx'

def main():
    raw_data = requests.get(target_url, auth=('huge', 'file')).content
    for x in range(5):
        with open(r'./%d.jpg' % x ,'wb') as file:
            file.write(raw_data[x::5])

if __name__ == '__main__':
    main()


# 运行结果挺慢的
'''
[Finished in 1.6s]
'''

