#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2018-05-16 13:48:22
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : level 11 of python challenge
# 
# 思路：这一关上来内容更简单，就一张模糊不清的图片，打开网页源代码发现什么也没有，后来发现<title>odd even</title>
#       其中标题中有两个单词odd和even，也就是奇数和偶数，去哪里去找奇数和偶数呢？整个网页中也就图片是一个可用的资源
#       难道奇数和偶数隐藏在图片中，开始考虑到取像素，但是真的不知道怎么按照奇数和偶数的规律取像素点，取完了又要做什么呢？
#       于是参考了网上大神的做法，原来是按奇偶行、奇偶列来进行像素取点，然后分解成两幅图片，假设原来有6X6=36个像素，那么
#       分解之后就变成了两个3X3=9个像素的新图片，这里可能会迷惑，36个像素分解两个图片应该为18个像素，但是那样就不是等比例了，
#       所以需要分成两个3X3的图片，那缺少的那部分像素从哪里来呢？实际上是分解图片中的每个像素被用了2次，
#       在图片cave.jpg中每四个像素为一组，a[0][0]、a[1,1]都是第一张图片中的[0][0]位置，a[0][1]、a[1][0]都是第二张图片中的[0][0]位置，
#       也就是每四个元素中对角线的两个位置是原图中的同一像素，两条对角线属于不同的两张图片，最后呈现的是棋盘状的划分
#       按照这个思路将像素点分成两个图片，然后显示出来，发现一张度与原图相似，另一张图片上有字母evil，便是下一关的url
#       如果不太明白像素是怎么划分的，可以使用本文件中的test函数测试
# 
# 备注：1. python challenge home page : http://www.pythonchallenge.com/
#       2. current level url : http://www.pythonchallenge.com/pc/return/5808.html
#       3. next level url : http://www.pythonchallenge.com/pc/return/evil.html
#       4. username:huge password:file

from PIL import Image
import requests
import io

# image url
target_url = 'http://www.pythonchallenge.com/pc/return/cave.jpg'

def get_two_pic():
    image_data = requests.get(target_url, auth=('huge', 'file')).content
    stream = io.BytesIO(image_data)
    img = Image.open(stream)
    #img.show();
    width = img.size[0]
    height = img.size[1]
    odd = Image.new(img.mode, (width//2, height//2))
    even = Image.new(img.mode, (width//2,height//2))
    for x in range(width):
        for y in range(height):
            pixel=img.getpixel((x,y))
            if (x+y)%2:
                odd.putpixel(((x-1)//2, y//2) if x%2 else (x//2, (y-1)//2) , pixel)
            else:
                even.putpixel((x//2, y//2),pixel)
    odd.show()
    even.show()


def test():
    for x in range(6):
        for y in range(6):
            if (x+y)%2:
                pass #print("(%d, %d, %d, %d)" % (x, y, (x-1)//2, y//2) if x%2 else (x, y, x//2, (y-1)//2))
            else:
                print("(%d, %d, %d, %d)" % (x, y, x//2, y//2))

def main():
    get_two_pic()
    #test()

if __name__ == '__main__':
    main()


# 运行结果还是很快的
'''
5808
[Finished in 0.2s]
'''

