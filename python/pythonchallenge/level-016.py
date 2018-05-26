#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2018-05-26 13:39:29
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : level 16 of python challenge
# 
# 思路：老样子，一张图，是一张模糊不清的图，其实不能够叫模糊不清，应该是雪花图，类似于老电视中信号很弱时的样子
#       打开源码发现只有标题是个线索let me get this straight，让我们来获得这条直线，直线在哪呢？我猜应该是在图片中
#       至此，卡壳，没法继续了，前去膜拜大神
#       看完了，就是把图片中那些短横线对齐，把短横线之前的像素移动到短横线之后，短横线的像素值大概在195
#       其实可以想象成推动各行像素，使得段红线排成一列就好了，每行像素是个环，最后出现的图像是一个单词romance
#       这就是通往下一关的url
# 
# 备注：1. python challenge home page : http://www.pythonchallenge.com/
#       2. current level url : http://www.pythonchallenge.com/pc/return/mozart.html
#       3. next level url : http://www.pythonchallenge.com/pc/return/romance.html
#       4. username:huge password:file
#

from PIL import Image
import requests
import io

target_url = 'http://www.pythonchallenge.com/pc/return/mozart.gif'

def get_source_image():
    image_date = requests.get(target_url, auth=('huge', 'file')).content
    stream = io.BytesIO(image_date)
    img = Image.open(stream)
    return img

def main():
    img = get_source_image();
    new_img = Image.new("RGB", img.size)
    for y in range(img.size[1]):
        line = [img.getpixel((x,y)) for x in range(img.size[0])]
        red_pos = 0
        while line[red_pos] != 195:
            red_pos += 1
        new_line = line[red_pos:] + line[:red_pos]
        for x in range(len(new_line)):
            new_img.putpixel((x, y), new_line[x])
    new_img.show()

if __name__ == '__main__':
    main()

# 运行结果
'''
[Finished in 4.6s]
'''
