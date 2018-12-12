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
    ('#FF0000','none/firewall',''),
    ('#008000','player',''),
    ('#00FF00','pet',''),
    ('#0000FF','',''),
    ('#FF00FF','monster',''),
    ('#FFFF00','',''),
    ('#00FFFF','',''),
    ('#800000','',''),
    ('#008080','boss',''),
    ('#FF8080','',''),
    ('#004040','',''),
    ('#80FFFF','',''),
    ('#FF8000','',''),
    ('#FF80FF','',''),
    ('#804040','',''),
    ('#FFFF80','',''),
    ('#FF8040','dialog',''),
    ('#00FF00','',''),
    ('#8080FF','',''),
    ('#808000','',''),
    ('#C0C0C0','',''),
    ('#800080','',''),
    ('#8000FF','',''),
    ('#0080C0','',''),
    ('#8080C0','',''),
    ('#80FF80','',''),
    ('#400000','',''),
    ('#408080','',''),
    ('#800040','',''),
    ('#FF0080','',''),
    ('#804000','',''),
    ('#004080','',''),
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

def dynamic_barrier_show(uiroot, color_list):
    grid_panel = ttk.LabelFrame(uiroot, text="dynamic barrier color plate")
    grid_panel.grid(column=0, row=0, padx=10, pady=10)
    index = 0
    row = -1
    col = 0
    for x in color_list:
        if index == 0:
             uiroot.configure(background=x[0])
             index += 1
             continue

        if (index & (index  - 1)) == 0:
            row +=1
            col = 0
        ttk.Label(grid_panel, background=x[0], width=7, text=x[1]).grid(column=col, row=row)
        col += 1
        index += 1



def main(showtype):
    root = Tk()
    root.title('color plate')
    # if showtype == "binary":
    #     binary_show(root, barrier_color_list);
    # else:
    #     normal_show(root, barrier_color_list);
    dynamic_barrier_show(root, barrier_color_list);
    root.mainloop()

if __name__=="__main__":
    main("binary")

