#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2022-11-20 17:05:49
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : pushplus简单使用

import requests
import pushutils

def send_wechat_msg(title, content):
    token = pushutils.get_token()
    url = 'http://www.pushplus.plus/send?token='+token+'&title='+title+'&content='+content
    requests.get(url)

if __name__ == "__main__":
    send_wechat_msg('python推送测试消息', '测试消息内容')
