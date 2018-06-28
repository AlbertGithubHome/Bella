#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2018-06-26 19:46:14
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : level 24 of python challenge
# 
# 思路：这一关的网页上这次是一张大图片，厉害了，看起来像是一张迷宫图，网页的标题为from top to bottom
#       除此之外没有其他的任何线索，图片的名字为maze.png，看起来有点用处，哦，原来maze是迷宫的意思，那看起来maze也没有用了
#       如果真的按标题所说，从上走到下，那眼睛还不得瞎了啊，肯定有一种python 的处理哲学在等着我，会是什么呢？
#       原来真的是要求走迷宫，算了，先写一个深度优先搜索搜一下吧，为什么不是广度，因为广度不好写。。。
#
#       注意这个图片还有一个干扰项，就是左上角的24这个数字，去掉这个干扰，需要从左上角(0,0)一直向右走，走到第一个像素为0的点，
#       也就是白色的部分，除去有干扰的部分，图片上的点非白即红，也就是说要不然RGB都为0，要不然只有GB两个分量为0，
#       图片的大小为641*641，我们只要沿着白色一直走到坐标(x,640)，那么就成功了
#       
#       前面这一段当我没说，其实白色的是墙，带颜色的像素为通道，我们只关注R通道就可以了，按照深度优先的算法走迷宫，
#       只要沿着非白色一直走到坐标(x,640)，把路径上的点的像素中R坐标保存到文件中，
#       费了九牛二虎之力终于把迷宫走完了，哎，还真是学了不少东西，比如可以通过循环来实现深度优先搜索，把收集到的数据输出到
#       文件中，打印数据的前20字节，前几个字节为b'\x00P\x00K\x00\x03，其中包含PK据说是zip文件，这里面还有一个坑，就是有很多0
#       那些数据是没有用的，需要剔除掉多出的0，删除后德奥b'PK\x03\x04\x14\x00，据说是zip文件了，解压后得到两个文件，一张图片
#       maze.jpg上有字母显示lake，这就是通往下一关的url，还有一个文件mybroken.zip，暂时还不知道有什么用
#       
#       
#       
#
# 备注：1. python challenge home page : http://www.pythonchallenge.com/
#       2. current level url : http://www.pythonchallenge.com/pc/hex/ambiguity.html
#       3. next level url : http://www.pythonchallenge.com/pc/hex/lake.html
#       4. curlevel username:butter password:fly
#

from PIL import ImageDraw
from PIL import Image
import requests
import zipfile
import io

# resource url
target_url = 'http://www.pythonchallenge.com/pc/hex/maze.png'
# 墙的像素
wall = (255, 255, 255, 255)
# 前进方向
walkdir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# 获得网站图像
def get_image_file():
    image_data = requests.get(target_url, auth=('butter', 'fly')).content
    stream = io.BytesIO(image_data)
    img = Image.open(stream)
    return img

# 找到进入点
def find_start_pos(img, width):
    for x in range(width-1, 0, -1):
        pixel_value = img.getpixel((x, 1));
        print(x, pixel_value)
        if pixel_value != wall:
            return x, 0
    return 0, 0

# 调试输出区域像素点
def output_pixel(img, start, end):
    for y in range(start, end):
        print("\n")
        for x in range(start, end):
            print(img.getpixel((x, y)))

# 输出R通道的数据文件，打印图像
def output_file(img, path):
    new_img = Image.new("RGB", img.size, 'black')
    draw = ImageDraw.Draw(new_img) #画图对象，对新图操作
    for poslist in path:
        for pos in poslist:
            draw.point([pos[0], pos[1]])
    new_img.show()

# 深度优先搜索路径，结果不行，超过了递归深度
# RecursionError: maximum recursion depth exceeded
def dfs(img, path, x, y):

    # 找到了，到达底部
    if y == img.size[1]:
        path.append((x, y))
        output_file(img, path)
        return True

    # 碰到了墙
    if img.getpixel((x, y)) == wall:
        return False

    # 走了回头路
    if len(path) >= 2 and path[-2] == (x, y):
        return False

    path.append((x, y))

    for cur_dir in walkdir:
        if dfs(img, path, x + cur_dir[0], y + cur_dir[1]):
            return True

    path.pop()
    return False

# 也算深度优先搜索，但是使用循环代替递归
def new_search(img, pos):
    path = []           # 整条路径
    footpath = []       # 小路，就是子路径
    find_path = False;  # 标记是否在找到
    end_y = img.size[1] - 1

    while pos[1] != end_y:          # 没到底继续找
        img.putpixel(pos, wall)     # 封死来路，免得绕回去
        path_count = 0              # 子路径的条数

        for cur_dir in walkdir:     # 四个方向查一遍有几条路径
            tmp_pos = (pos[0] + cur_dir[0], pos[1] + cur_dir[1])
            try:
                if img.getpixel(tmp_pos) != wall:
                    path_count += 1
                    new_pos = tmp_pos
            except: #越界像素不作处理
                pass

        if path_count == 1:
            footpath.append(pos)
            pos = new_pos
        elif path_count == 0:
            if footpath == []:
                try:
                    footpath = path.pop()
                except:
                    print(path)
                    break; # 说明没找到路
            pos = footpath[0];
            footpath = []
        else:
            if len(footpath) > 0:
                path.append(footpath);
            footpath = [pos]
            pos = new_pos
    else:
        find_path = True
        footpath.append(pos)
        path.append(footpath)

    if find_path:
        return path
    else:
        return []


def main():
    img = get_image_file()
    #img.show()
    print("image size:", img.size, type(img.size))
    start_pos = find_start_pos(img, img.size[0]);
    print("start_x, starty = ", start_pos[0], start_pos[1])
    #output_pixel(img, 100, 105)
    path = new_search(img, start_pos);
    if len(path) == 0:
        print("no way!")
    else:
        #print(path)
        output_file(img, path)
        img = get_image_file()
        data = [img.getpixel(pos)[0] for footpath in path for pos in footpath]
        bytes_data = bytes(data[1::2])
        print(str(bytes_data)[:20])
        zip_file = zipfile.ZipFile(io.BytesIO(bytes_data))
        zip_file.extractall('./out24')


if __name__ == '__main__': main()

# 输出图片大小和起始位置
'''
image size: (641, 641) <class 'tuple'>
640 (255, 255, 255, 255)
639 (80, 0, 0, 255)
start_x, starty =  639 0
[Finished in 7.0s]
'''