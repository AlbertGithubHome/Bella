#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2018-06-25 15:51:28
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : level 22 of python challenge
# 
# 思路：这一关回归了正常，解题线索是一个网址，页面上有一个张图片，图片显示的貌似是一个带摇杆的手柄，标题为emulate
#       也就是仿真、模拟的意思，源代码中还有一行注释<!-- or maybe white.gif would be more bright-->，试着访问了
#       一下http://www.pythonchallenge.com/pc/hex/white.gif，果然可以打开，但是图片显示是黑色的，没有再找到其他线索
#       可能需要分析gif图片的像素，终于又看了大神们的答案，其实就是把gif图像中的每一帧都展开，取出其中与周围像素不同的点，
#       将找到的这些点依次连线就会找到答案，实际上这些点就是摇杆滑动的轨迹，看到答案后一切都明白了，最后得到一串字母，bonus
#       这就是通往下一关的url
#       
#       其实每个像素点表示的是运动的方向，是个向量
#       
#       
#
# 备注：1. python challenge home page : http://www.pythonchallenge.com/
#       2. current level url : http://www.pythonchallenge.com/pc/hex/copper.html
#       3. next level url : http://www.pythonchallenge.com/pc/hex/bonus.html
#       4. curlevel username:butter password:fly
#

from PIL import ImageDraw
from PIL import Image
import requests
import io


# resource url
target_url = 'http://www.pythonchallenge.com/pc/hex/white.gif'

def get_image_file():
    image_data = requests.get(target_url, auth=('butter', 'fly')).content
    stream = io.BytesIO(image_data)
    img = Image.open(stream)
    return img

def main():
    img = get_image_file()
    new_img = Image.new("RGB", img.size)
    draw = ImageDraw.Draw(new_img) #画图对象，对新图操作
    print(img.size, img.n_frames)  #打印图像大小和帧数

    center_x, center_y = 0, 100
    for frame in range(img.n_frames):
        img.seek(frame)
        left, top, right, bottom = img.getbbox() # 获得图像的包围盒
        print(left, top, right, bottom)

        px, py = (left - 100) // 2, (top - 100) // 2
        if px == py == 0:
            center_x, center_y = center_x + 30, 100 # 确定一个新的图形中心

        center_x, center_y = center_x + px, center_y + py
        draw.point([center_x, center_y])

    new_img.show();


if __name__ == '__main__':
    main()

# 图像大小
'''
(200, 200)
[Finished in 1.3s]
'''

# 所有像素点信息
'''
(200, 200) 133
100 100 101 101
100 102 101 103
100 102 101 103
100 102 101 103
100 102 101 103
100 102 101 103
100 102 101 103
100 102 101 103
100 102 101 103
102 102 103 103
102 100 103 101
102 100 103 101
102 100 103 101
102 100 103 101
102 100 103 101
102 100 103 101
102 100 103 101
102 98 103 99
100 98 101 99
100 98 101 99
100 98 101 99
98 98 99 99
98 100 99 101
98 100 99 101
98 100 99 101
98 100 99 101
98 100 99 101
98 100 99 101
98 102 99 103
100 100 101 101
98 98 99 99
98 98 99 99
98 100 99 101
98 100 99 101
98 100 99 101
98 100 99 101
98 100 99 101
98 102 99 103
98 102 99 103
98 102 99 103
100 102 101 103
100 102 101 103
102 102 103 103
102 102 103 103
102 102 103 103
102 100 103 101
102 100 103 101
102 100 103 101
102 100 103 101
102 100 103 101
102 98 103 99
102 98 103 99
102 98 103 99
100 98 101 99
100 98 101 99
100 100 101 101
100 102 101 103
100 102 101 103
100 102 101 103
100 102 101 103
100 102 101 103
100 102 101 103
100 102 101 103
102 100 103 101
100 98 101 99
100 98 101 99
100 98 101 99
102 98 103 99
102 98 103 99
102 98 103 99
102 98 103 99
102 100 103 101
102 100 103 101
102 102 103 103
102 102 103 103
102 102 103 103
100 102 101 103
100 102 101 103
100 102 101 103
100 102 101 103
100 100 101 101
100 102 101 103
100 102 101 103
100 102 101 103
100 102 101 103
100 102 101 103
100 102 101 103
102 102 103 103
102 100 103 101
102 100 103 101
102 100 103 101
102 100 103 101
102 100 103 101
102 100 103 101
102 98 103 99
100 98 101 99
100 98 101 99
100 98 101 99
100 98 101 99
100 98 101 99
100 98 101 99
100 100 101 101
98 98 99 99
98 100 99 101
98 100 99 101
98 100 99 101
98 100 99 101
98 100 99 101
98 100 99 101
98 100 99 101
98 102 99 103
100 102 101 103
100 102 101 103
102 102 103 103
102 100 103 101
102 100 103 101
102 100 103 101
102 100 103 101
102 100 103 101
102 100 103 101
102 100 103 101
102 102 103 103
100 102 101 103
100 102 101 103
98 102 99 103
98 100 99 101
98 100 99 101
98 100 99 101
98 100 99 101
98 100 99 101
98 100 99 101
98 100 99 101
98 98 99 99
[Finished in 2.8s]
'''
