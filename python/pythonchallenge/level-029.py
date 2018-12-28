#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2018-12-25 15:10:00
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : level 29 of python challenge
# 
# 思路：开篇一张图，内容全靠猜，网页题目silence！也就是沉默，图片上的内容很像防毒面具，其实是一个用水杯、
#       眼镜、镜子组成的，旁边还有一个画着小黄鸡的靠枕，另一边是一瓶啤酒，图片的名字是whoisit.jpg好像在问：
#       他是谁？连起来看就是一个拥有的者沉默技能和防毒面罩的人是谁呢？我真的不知道!
#       
#       听高人说是要分析网页源码中的空格，把每行空格的个数转换成字节，然后输出试试，得到了以下信息
#       b'BZh91AY&SY\xd9\xc2p\x18\...，看来是压缩过的，使用bz2解压试试，得到信息Isn't it clear? I am yankeedoodle!
#       看来和yankeedoodle有关，
#       
#       搜索单词含义是：扬基歌（美国独立战争时流行的一首歌曲），通往下一关的地址就是yankeedoodle，可是这和yankeedoodle
#       有什么关系，这一关的图片又有什么用？不得而知!
#       
#
# 备注：1. python challenge home page : http://www.pythonchallenge.com/
#       2. current level url : http://www.pythonchallenge.com/pc/ring/guido.html
#       3. next level url : http://www.pythonchallenge.com/pc/ring/yankeedoodle.html
#       4. curlevel username:repeat password:switch
#

import requests
import bz2

# html url
target_url = 'http://www.pythonchallenge.com/pc/ring/guido.html'

def download_image():
    html_data = requests.get(target_url, auth=('repeat', 'switch')).content
    html_str = html_data.decode();
    html_str = html_str[html_str.find("</html>\n") + len("</html>\n"):]
    #print(html_str)
    return html_str

def main():
    blank_str = download_image()
    blank_list = blank_str.split("\n")
    #print(blank_list)
    data = bytes([len(x) for x in blank_list])
    print(data)
    print(bz2.decompress(data))

if __name__ == '__main__': main()


# 将空格数对应的字节整理到一起得到一串以BZ开头的的信息
'''
b'BZh91AY&SY\xd9\xc2p\x18\x00\x00\x04\x9d\x80`\x80\x00\x00\x80 ./\x9c  \x001L\x98\x99\x06F\x112hd
\x06jUd\xb9\x9e\xc6\x18\xc5\x92RH\xe5Z"\x01\xba\xa7\x80\x7f\x8b\xb9"\x9c(Hl\xe18\x0c\x00\x00'
[Finished in 0.6s]
'''

# 解压信息
'''
b"Isn't it clear? I am yankeedoodle!"
'''