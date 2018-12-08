#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2018-12-07 18:00:34
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : make color plate
# 
# 思路：通过tkinter库在界面上添加标签并设置成对应颜色

from tkinter import *
from tkinter import ttk

barrier_color_list = [
    '#00FF20',
    '#800020',
    '#FF0020',
    '#000020',
    '#00FF20',
    '#FFFF20',
    '#FF0020',
    '#008020',
    '#800020',
    '#80FF20',
    '#400020',
    '#FF8020',
    '#80FF20',
    '#80FF20',
    '#408020',
    '#FFFF20',
    '#80FF20',
    '#FF0020',
    '#808020',
    '#808020',
    '#C0C020',
    '#008020',
    '#008020',
    '#800020',
    '#808020',
    '#FF8020',
    '#004020',
    '#804020',
    '#008020',
    '#00FF20',
    '#408020',
    '#400020',
]

def normal_show(uiroot, color_list):
    for x in color_list:
        Label(uiroot, bg=x, width=35, height=1, text='hello world').pack()

def binary_show(uiroot, color_list):
    grid_panel = ttk.LabelFrame(uiroot, text="binary barrier color plate")
    grid_panel.grid(column=0, row=0, padx=10, pady=10)
    index = 0
    row = -1
    col = 0
    for x in color_list:
        if index == 0:
             uiroot.configure(background=x)
             index += 1
             continue

        if (index & (index  - 1)) == 0:
            row +=1
            col = 0
        ttk.Label(grid_panel, background=x, width=10, text="hello world").grid(column=col, row=row)
        col += 1
        index += 1



def main(showtype):
    root = Tk()
    root.title('color plate')
    if showtype == "binary":
        binary_show(root, barrier_color_list);
    else:
        normal_show(root, barrier_color_list);
    root.mainloop()

if __name__=="__main__":
    main("binary")

