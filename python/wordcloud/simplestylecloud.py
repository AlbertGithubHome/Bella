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

# fas fa-cat
# fas fa-crown
# fas fa-bug
# fas fa-dog

import jieba
from stylecloud import gen_stylecloud

def jieba_cloud(output_file_name, icon, file_name):
    with open(file_name, 'r', encoding='utf8') as f:
        word_list = jieba.cut(f.read())
        word_result = " ".join(word_list)

        #制作中文云词
        gen_stylecloud(text=word_result, icon_name=icon,
            font_path='C:\\Windows\\Fonts\\simhei.ttf',
            output_name='stylelist/' + str(output_file_name) + '.png')  #必须加中文字体，否则格式错误

if __name__ == "__main__":
    #jieba_cloud(1, 'fas fa-cat', '../../../gitee/blog/source/_posts/小白眼中的docker究竟是个什么东西.md')
    #jieba_cloud(2, 'fas fa-bug', '../../../gitee/blog/source/_posts/GDB调试指北-启动GDB并查看说明信息.md')
    #jieba_cloud(4, 'fas fa-crow', '../../../gitee/blog/source/_posts/Redis源码-BFS方式浏览main函数.md')
    jieba_cloud(5, 'fas fa-chart-line', '../../../gitee/blog/source/_posts/git-log根据特定条件查询日志并统计修改的代码行数.md')