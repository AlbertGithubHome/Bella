#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2022-11-20 17:05:49
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : pushplus使用Post方式推送图片信息

import sys
import datetime
import requests
import pushutils

def get_content(today, imgs):
    content = ""
    img_list = imgs.split(' ')
    for img in img_list:
        one_img = "<br/><img src='http://rlotflz4b.hn-bkt.clouddn.com/{0}/{1}' />".format(today, img)
        print(one_img)
        #content += "<br/><img src='https://cdn.jsdelivr.net/gh/albertgithubhome/cdn/img/analyze/stock/{0}/{1}' />".format(today, img)
        #content += "<br/> https://cdn.jsdelivr.net/gh/albertgithubhome/cdn/img/analyze/stock/{0}/{1}".format(today, img)
        #content += "<br/>[{0}](https://cdn.jsdelivr.net/gh/albertgithubhome/cdn/img/analyze/stock/{1}/{2}) ".format(img, today, img)
        content += one_img
    return content

def post_wechat_msg(token, title, content):
    url = 'http://www.pushplus.plus/send'
    new_json = {
        "token": token,
        "title": title,
        "content": content,
        "topic": "9caigroup",
        #"template": "markdown"
    }
    result = requests.post(url,json=new_json)
    print(result)

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("argv error")
    else:
        today = datetime.datetime.now().strftime('%Y%m%d')
        imgs = sys.argv[1]

        tk = pushutils.get_token()
        ct = get_content(today, imgs)
        if tk:
            print(tk)
            print(ct)
            post_wechat_msg(tk, '{0}-技术分析'.format(today), ct)
