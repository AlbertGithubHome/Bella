#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2018-01-03 14:27:32
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : a test for swiping screen

import time,os

def try_swipe(x, y, press_time):
    cmd = 'adb shell input swipe {x1} {y1} {x2} {y2} {valid_time}'.format(
        x1 = x,
        y1 = y,
        x2 = x,
        y2 = y,
        valid_time = press_time)

    print("cmd=%s" % cmd)
    os.system(cmd)

def simulate_swipe():
    for x in range(1,6):
        print("simulate times:%s" % x)
        try_swipe(x * 200, x * 400, 100)
        time.sleep(4)

if __name__ == '__main__':
    simulate_swipe()