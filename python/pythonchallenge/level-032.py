#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-01-04 10:07:40
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
# @Subject  : level 32 of python challenge
#
# 思路：页面内容终于不是一张图片了，看似一个点击方块的游戏，网页标题为etch-a-scetch，其中包含两个css文件
#       和两个js文件，下面就是提示消息了<!-- you are in level 32 -->告诉你现在已经是第32关了
#
#        Fill in the blanks <!-- for warmup.txt -->是说填上这些空白，用来寻找warmup.txt 文件，究竟怎么填，
#        我还没有弄明白呢
#
#        看来真得好好学学英语了，居然把因果关系弄反了，不是填格子找warmup.txt，而是通过warmup.txt找到
#        填格子的要求，将网址结尾改为warmup.txt得到填写要求的文件，接下来的任务就是根据要求找到填写结果
#        # Dimensions
#        9 9
#
#        # Horizontal
#        2 1 2
#        1 3 1
#        5
#
#        7
#        9
#        3
#
#        2 3 2
#        2 3 2
#        2 3 2
#
#        # Vertical
#        2 1 3
#        1 2 3
#        3
#
#        8
#        9
#        8
#
#        3
#        1 2 3
#        2 1 3
#
#       根据这些神秘的数字，填出来一个类似于箭头的形状，注意Horizontal是左边一侧的数字，Vertical是上面一行的数字
#   ·   填完的形状大概这样：
#
#       ■■□□■□□■■
#       ■□□■■■□□■
#       □□■■■■■□□
#       □■■■■■■■□
#       ■■■■■■■■■
#       □□□■■■□□□
#       ■■□■■■□■■
#       ■■□■■■□■■
#       ■■□■■■□■■
#
#       这是一个向上的箭头，根据大神们提醒应该是单词up，所以尝试访问文件up.txt
#       view-source:http://www.pythonchallenge.com/pc/rock/up.txt
#       文本很多，如下：
#       # Dimensions
#       32 32
#
#       # Horizontal lines
#       3 2
#       8
#       10
#       3 1 1
#
#       5 2 1
#       5 2 1
#       4 1 1
#       15
#
#       19
#       6 14
#       6 1 12
#       6 1 10
#
#       7 2 1 8
#       6 1 1 2 1 1 1 1
#       5 1 4 1
#       5 4 1 4 1 1 1
#
#       5 1 1 8
#       5 2 1 8
#       6 1 2 1 3
#       6 3 2 1
#
#       6 1 5
#       1 6 3
#       2 7 2
#       3 3 10 4
#
#       9 12 1
#       22 1
#       21 4
#       1 17 1
#
#       2 8 5 1
#       2 2 4
#       5 2 1 1
#       5
#
#       # Vertical lines
#       5
#       5
#       5
#       3 1
#
#       3 1
#       5
#       5
#       6
#
#       5 6
#       9 5
#       11 5 1
#       13 6 1
#
#       14 6 1
#       7 12 1
#       6 1 11 1
#       3 1 1 1 9 1
#
#       3 4 10
#       8 1 1 2 8 1
#       10 1 1 1 7 1
#       10 4 1 1 7 1
#
#       3 2 5 2 1 2 6 2
#       3 2 4 2 1 1 4 1
#       2 6 3 1 1 1 1 1
#       12 3 1 2 1 1 1
#
#       3 2 7 3 1 2 1 2
#       2 6 3 1 1 1 1
#       12 3 1 5
#       6 3 1
#
#       6 4 1
#       5 4
#       4 1 1
#       5
#
#       这个可麻烦了，暂时没解决，偷个懒，据说解出来是一条蛇，尝试访问python.html
#       图片显示了一条可爱的蛇，并且还有一条提示信息：
#       Congrats! You made it through to the smiling python.
#       "Free" as in "Free speech", not as in "free...
#       查了wiki百科https://en.wikipedia.org/wiki/Gratis_versus_libre#.22Free_beer.22_vs_.22free_speech.22_distinction
#       其中有一句"Free beer" vs "freedom of speech" distinction，所以尝试 beer.html 页面，bingo，过了
#       成功到达33关
#
#
#
#
# 备注：1. python challenge home page : http://www.pythonchallenge.com/
#       2. current level url : http://www.pythonchallenge.com/pc/rock/beer.html
#       3. next level url : http://www.pythonchallenge.com/pc/rock/arecibo.html
#       4. curlevel username:kohsamui password:thailand
#

import requests

# file url
target_url = 'http://www.pythonchallenge.com/pc/rock/up.txt'

def download_data():
    txt_data = requests.get(target_url, auth=('kohsamui', 'thailand')).content
    with open('32/up.txt', 'wb') as file:
        file.write(txt_data)

def main():
    download_data

if __name__ == '__main__': main()




# 这一关并未用python解，看起来更像是算法题，后续用python实现下吧
'''
[Finished in 0.0s]
'''