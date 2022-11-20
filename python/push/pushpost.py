#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2022-11-20 17:05:49
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : pushplus使用Post方式推送

import requests
import pushutils

def post_wechat_msg(token, title, content):
    url = 'http://www.pushplus.plus/send'
    new_json = {
        "token": token,
        "title": title,
        "content": content,
        "topic": "9caigroup"
    }
    result = requests.post(url,json=new_json)
    print(result)

if __name__ == "__main__":
    tk = pushutils.get_token()
    ct = pushutils.get_content();
    if tk:
        print(tk)
        print(ct)
        post_wechat_msg(tk, '北京天气预报', ct)
