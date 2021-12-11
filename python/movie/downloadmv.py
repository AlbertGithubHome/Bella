#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#a test for making picture

import time
import requests

with open('movie.html', 'w', encoding='utf-8') as file:
    res = requests.get("http://m.huigutongying.cn/play/17719-0-0.html")
    file.write(res.text)
    #print(res.)

l = time.localtime(time.time())
print(l.tm_hour)

if l.tm_hour in [23, 0, 1, 2, 3, 4, 5, 6, 7]:
    print(True)

def is_code_night():
    l = time.localtime(time.time())
    if l.tm_hour in [23, 0, 1, 2, 3, 4, 5, 6, 7]:
        return True

    return False