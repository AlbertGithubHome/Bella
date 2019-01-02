#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2018-12-29 09:52:06
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : level 31 of python challenge
# 
# 思路：一张海边的图片，场景正中间是一块石头，看起来像是孙猴子出生的那一块，没有看到其他有用的信息
#       然后就是图片实际上有一个超链接，链接到网页../rock/grandpa.html，这应该就是下一关的网址，但是需要
#       账号和密码，这一关的任务应该就是找账号和密码了
#       
#       这一关的标题为Where am I？应该是需要解答我在哪？
#       点击下一关的链接，出来的提示中有--该网站称：“island : country”，源码注释中包含信息:
#       <!-- short break, this ***REALLY*** has nothing to do with Python -->
#       短暂休息，this真的什么都没做，这个着重强调的REALLY有什么含义，又看到了this，难道这一关又和this库有关
#       难不成还有个REALLY库？
#       
#       看了大神的解答，才明白了注释的含义，是说这一关的信息真的没有用，账号密码根据提示和图片应该
#       是用户名kohsamui，密码thailand，输入即可打开网页，但是还是在31关，然后非常气人的给出了提示
#       That was too easy. You are still on 31...
#       
#       图片内容是一片类似于雪花的闪电链，源码标题为UFOs ?，看起来和外星人有关了，这一关图片的名字为
#       mandelbrot.gif，是一个人名--曼德尔布罗特，网上搜索后发现还有一种图像是这个名字，mandelbrot图像，
#       “Mandelbrot图像中的每个位置都对应于公式N=x+y*i中的一个复数。其实数部分是x，虚数部分是y，
#       i是-1的平方根。图像中各个位置的x和y坐标对应于虚数的x和y部分。看来是需要通过这个公式来分析
#       这个图像了
#       
#       图像的周围还有一些格式符：
#       <window left="0.34" top="0.57" width="0.036" height="0.027"/>
#       <option iterations="128"/>
#       
#       根据所给的参数和曼德勃罗公式生成一幅图片，结果与原图片是上下颠倒的，使用函数上下反转，得到几乎一样的两张图
#       把其中不等的内容输出为一幅图，据说是Arecibo message相关，打开看看链接确实很像，通往下一关的链接就是arecibo
#       这一关过的糊里糊涂的
#
# 备注：1. python challenge home page : http://www.pythonchallenge.com/
#       2. current level url : http://www.pythonchallenge.com/pc/ring/grandpa.html
#       3. next level url : http://www.pythonchallenge.com/pc/rock/arecibo.html
#       4. curlevel username:repeat password:switch
#       5. curlevel username:kohsamui password:thailand
#

import requests
from PIL import Image

# file url
target_url = 'http://www.pythonchallenge.com/pc/rock/mandelbrot.gif'

def download_image():
    image_data = requests.get(target_url, auth=('kohsamui', 'thailand')).content
    with open('31/mandelbrot.gif', 'wb') as file:
        file.write(image_data)

def main():

    img = Image.open("31/mandelbrot.gif")

    left = 0.34
    bottom = 0.57
    width = 0.036
    height = 0.027
    iterations = 128

    w, h = img.size
    xstep = width / w
    ystep = height/ h

    result = []

    for y in range(h):
        for x in range(w):
            c = complex(left + x * xstep, bottom + y * ystep)
            z = 0 + 0j
            for i in range(iterations):
                z = z * z + c
                if abs(z) > 2: 
                    break
            result.append(i)

    img2 = img.copy()
    img2.putdata(result)
    img2 = img2.transpose(Image.FLIP_TOP_BOTTOM)
    #img2.show()

    diff = [(a - b) for a, b in zip(img.getdata(), img2.getdata()) if a != b]
    print(len(diff))

    new_img = Image.new('L', (23, 73))
    new_img.putdata([(i < 16) and 255 or 0 for i in diff])
    new_img.resize((230,730)).show()



if __name__ == '__main__': main()




# 不一样的信息数量，分解为23*73
'''
1679
[Finished in 7.5s]
'''