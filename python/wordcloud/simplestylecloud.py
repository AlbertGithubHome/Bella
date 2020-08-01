#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2020-8-1 14:15:21
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : 使用stylecloud做一个美化词云

# icon_name 参数在以下两个网站上找，替换后面的名字即可
# https://fa5.dashgame.com/#/%E5%9B%BE%E6%A0%87
# https://fontawesome.dashgame.com/

import jieba
from stylecloud import gen_stylecloud

def jieba_cloud(output_file_name, file_name):
    with open(file_name, 'r', encoding='utf8') as f:
        word_list = jieba.cut(f.read())
        word_result = " ".join(word_list)

        #制作中文云词
        gen_stylecloud(text=word_result, icon_name='fas fa-cat',
            font_path='C:\\Windows\\Fonts\\simhei.ttf',
            output_name='stylelist/' + str(output_file_name) + '.png')  #必须加中文字体，否则格式错误

if __name__ == "__main__":
    jieba_cloud(1, '../../../gitee/blog/source/_posts/小白眼中的docker究竟是个什么东西.md')