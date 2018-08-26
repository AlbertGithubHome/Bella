#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2018-08-26 10:40:13
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : simulation to watch news

import os
import time

# 截屏取点
def pull_screenshot():
    os.system('adb shell screencap -p /sdcard/auto_screen.png')
    os.system('adb pull /sdcard/autojump.png .')

# 点击屏幕
def click(x1,y1,x2,y2,swipe_time,pause_time,info):
    cmd = 'adb shell input swipe {0} {1} {2} {3} {4}'.format(x1,y1,x2,y2,swipe_time);
    print('{0} => {1}, pause_time = {2}'.format(info, cmd, pause_time))
    os.system(cmd)
    if pause_time > 0: time.sleep(pause_time)

# 模拟点击屏幕
def simulation_click():
    x,y = 500,550
    return_x, return_y = 80,140
    refresh_x, refresh_y = 100,140
    from_x,from_y,to_x,to_y = 550,1000,550,350

    click(refresh_x, refresh_y, refresh_x, refresh_y, 800, 5, "refresh news list") # 刷新新闻
    for n in range(4):
        click(x, y, x, y, 500, 8, "watch news") # 选择新闻进入
        for k in range(3):
            click(from_x, from_y, to_x, to_y, 900, 2, "change page") # 向上滑动翻看

        click(return_x,return_y, return_x, return_y, 500, 5, "return main") # 点击返回按钮
        y += 300
        
# 模拟主循环
def main(max_count):
    count = 0
    while count < max_count:
        simulation_click()
        time.sleep(2)
        count += 1
        print('refresh count = {0}'.format(count))

if __name__ == '__main__':
    main(10)