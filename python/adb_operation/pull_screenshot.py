#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2018-01-03 14:33:33
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : a test for pulling a screenshot of phone

import os
import subprocess

screenshot_way = 0

def try_screenshot():
    global screenshot_way
    if screenshot_way == 2 or screenshot_way == 1:
        process = subprocess.Popen('adb shell screencap -p', shell=True, stdout=subprocess.PIPE)
        screenshot = process.stdout.read()
        if screenshot_way == 2:
            binary_screenshot = screenshot.replace(b'\r\n', b'\n')
        else:
            binary_screenshot = screenshot.replace(b'\r\r\n', b'\n')

        if len(screenshot) > 0:
            with open('autojump.png', 'wb') as file:
                file.write(binary_screenshot)
                file.close()
    elif screenshot_way == 0:
        os.system('adb shell screencap -p /sdcard/autojump.png')
        os.system('adb pull /sdcard/autojump.png .')

def pull_screenshot():
    os.system('adb shell screencap -p /sdcard/autoscreen.png')
    os.system('adb pull /sdcard/autoscreen.png .')

if __name__ == '__main__':
    pull_screenshot()