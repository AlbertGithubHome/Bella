#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2018-04-14 16:01:15
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : level 2 of python challenge
# 
# 思路：这一关相对第1关来说还容易一点，前后一共花了大约10分钟，如果真的是图片识别文字就难了
#       可根据题目来说还可以从源码中找答案，这就简单了，于是打开源码发现其中有这样一句话
#       'find rare characters in the mess below:'从这句开始后面就是一团乱麻了，也就是从这对字符中找字母
#       方法很简单，就是先利用requests库发送get请求，取到网页内容，通过字符串查找函数找到一段乱麻的位置
#       从乱麻开始位置逐步遍历，利用isalpha函数查找这团字符中的字母，然后拼接到一起就可以了。
#       其中包含的字母就是equality
# 
# 备注：1. python challenge home page : http://www.pythonchallenge.com/
#       2. current level url : http://www.pythonchallenge.com/pc/ocr/map.html
#       3. next level url : http://www.pythonchallenge.com/pc/def/equality.html


import requests

# entrance url
target_url = 'http://www.pythonchallenge.com/pc/def/ocr.html'

# get html page source code
def get_html_source_code():
    html = requests.get(target_url).content
    return html.decode('utf8');

def find_next_url(code_str):
    alpha = '';
    for x in code_str:
        if x.isalpha():
            alpha = alpha + x;
    return alpha;

def main():
    html_content = get_html_source_code();
    start_index = html_content.find('$@_$^__#)')
    code_content = html_content[start_index:-1]
    next_url = find_next_url(code_content)
    print('alpha is', next_url)

if __name__ == '__main__':
    main()

# 运行结果
'''
alpha is equality
[Finished in 1.2s]
'''