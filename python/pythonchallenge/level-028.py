#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2018-12-21 15:21:43
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : level 28 of python challenge
# 
# 思路：网页上又是一张图，看起来像黄果树瀑布，隐隐约约可以看到画面山有3个人，丛林密布
#       有很多水，再没有发现更多有用的信息，查看网页源码，发现图片的名字为bell.png，网页标题为
#       many pairs ring-ring，图片下面还有醒目的提示文字RING-RING-RING say it out loud
#       
#       联系在一起好像是铃铛叮铃铃的响，让我大声的喊出叮铃铃的声音有什么玄机？
#       传说RING-RING-RING读着读着会变成green。反正我是我感觉出来，发出来的倒像是reen，
#       接着访问green.html会提示“yes! green!”，试着输出图片的绿色通道，很明显会输出一大串数字
#       
#       网页的标题是many pairs ring-ring，也就是和成对有关，把绿色通道中的数字两两相减发现很多结果的绝对值均为42，
#       然后把相减不是42的字节收集起来(收集的差值的绝对值)，得到的字节以字符串显示，结果为whodunnit().split()[0] ?
#       
#       法语：谁是凶手？分片后取第一个元素，参考大神的说法Python的作者是Guido van Rossum，所以是guido，对于这个解释
#       我也是服了，为什么不能是其他人....
#
# 备注：1. python challenge home page : http://www.pythonchallenge.com/
#       2. current level url : http://www.pythonchallenge.com/pc/ring/bell.html
#       3. next level url : http://www.pythonchallenge.com/pc/ring/guido.html
#       4. curlevel username:repeat password:switch
#

from PIL import Image
import requests
import io

# image url
target_url = 'http://www.pythonchallenge.com/pc/ring/bell.png'

def download_image():
    image_data = requests.get(target_url, auth=('repeat', 'switch')).content
    stream = io.BytesIO(image_data)
    img = Image.open(stream)
    #img.show();
    return img

def main():
    img = download_image()
    green_data = [data[1] for data in img.getdata()]
    #print(green_data)
    result = [];
    for x in range(0, len(green_data), 2):
        diff = abs(green_data[x] - green_data[x + 1])
        if diff != 42:
            result.append(diff)
    print(bytes(result).decode());
    print("Guido van Rossum".split()[0]);




if __name__ == '__main__': main()


# 差值绝对值不为42的差值绝对值组合在一起
'''
whodunnit().split()[0] ?
[Finished in 3.8s]
'''