#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2022-11-20 17:05:49
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : 获取token工具

def get_token():
    with open('token', 'r') as file:
        tk = file.read(-1);
        return tk
    return ""

def get_content():
    with open('content', 'r', encoding='utf-8') as file:
        tk = file.read(-1);
        return tk
    return ""
