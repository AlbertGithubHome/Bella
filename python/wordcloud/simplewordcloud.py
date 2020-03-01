#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2020-03-01 22:13:22
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : 做一个简单的词云

import re
from PIL import Image
import matplotlib.pyplot as plt

import jieba # 结巴分词
import wordcloud # 词云展示库
import collections # 词频统计库
import numpy as np # numpy数据处理库

def get_text():
    with open('../albert_learn_lib.py', 'r', encoding='UTF-8') as file:
        content_data = file.read() # 读出整个文件
        pattern = re.compile(u'\t|\n|\.|-|:|;|\)|\(|\?|"') # 定义正则表达式匹配模式
        content_data = re.sub(pattern, '', content_data) # 将符合模式的字符去除
        return content_data

def output_image():

    string_data=get_text()
    # 文本分词
    seg_list_exact = jieba.cut(string_data, cut_all = False) # 精确模式分词
    object_list = []
    remove_words = [u'的', u'，',u'和', u'是', u'随着', u'对于', u'对',u'等',u'能',u'都',u'。',u' ',u'、',u'中',u'在',u'了',
                    u'通常',u'如果',u'我们',u'需要'] # 自定义去除词库

    for word in seg_list_exact: # 循环读出每个分词
        if word not in remove_words: # 如果不在去除词库中
            object_list.append(word) # 分词追加到列表

    # 词频统计
    word_counts = collections.Counter(object_list) # 对分词做词频统计
    word_counts_top10 = word_counts.most_common(10) # 获取前10最高频的词
    print (word_counts_top10) # 输出检查

    # 词频展示
    mask = np.array(Image.open('bg.png')) # 定义词频背景
    wc = wordcloud.WordCloud(
        font_path='C:/Windows/Fonts/simhei.ttf', # 设置字体格式
        #background_color="white",
        mask=mask, # 设置背景图
        max_words=200, # 最多显示词数
        max_font_size=100 # 字体最大值
    )

    wc.generate_from_frequencies(word_counts) # 从字典生成词云
    image_colors = wordcloud.ImageColorGenerator(mask) # 从背景图建立颜色方案
    wc.recolor(color_func=image_colors) # 将词云颜色设置为背景图方案
    plt.imshow(wc) # 显示词云
    plt.axis('off') # 关闭坐标轴
    plt.show() # 显示图像

if __name__ == '__main__':
    output_image()