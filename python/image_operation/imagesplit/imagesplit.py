#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2020-2-4 10:54:44
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : split images

import os
import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename

def imsplit(input_file_name, row_part, col_part):
    img = Image.open(input_file_name)
    w, h = img.size
    print('width = %d, height = %d' % (w, h))

    file_path,temp_file_name = os.path.split(input_file_name)
    file_name,ext = os.path.splitext(temp_file_name)

    avg_width_pixel = w // col_part
    avg_height_pixel = h // row_part

    for r in range(row_part):
        for c in range(col_part):
            end_width_pixel = (c + 1) * avg_width_pixel if c < col_part - 1 else w
            end_height_pixel = (r + 1) * avg_height_pixel if c < row_part - 1 else h
            box = (c * avg_width_pixel, r * avg_height_pixel, end_width_pixel, end_height_pixel)
            output_file = os.path.join(file_path, file_name + '_' + str(r) + '_' + str(c) + ext)
            print(output_file)
            img.crop(box).save(output_file, 'JPEG' if ext.lower() == '.jpg' else ext.upper()[1:])


def main():
    root = Tk()
    #设置窗口的大小宽x高+偏移量
    root.geometry('500x300+500+200')
    #设置窗口标题
    root.title('图片切割程序')
    # root.overrideredirect(1)
    #设置窗口图标
    # root.iconbitmap('spider_128px_1169260_easyicon.net.ico')
    root.mainloop()


main_w = 800
main_h = 600
class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, width=main_w, height=main_h)
        self.main_w = main_w
        self.main_h = main_h
        self.pack()

        self.path=tk.StringVar()
        tk.Entry(self,state='readonly',text=self.path).grid(row=0,column=0,columnspan=2,sticky=tk.E+tk.W)
        tk.Button(self,text='选择图片',command=self.choose_pic).grid(row=1,column=0)
        tk.Button(self,text='进行切割',command=self.img_split).grid(row=1,column=1)

    def choose_pic(self):
        self.img_path=askopenfilename()
        try:
            self.show_image();
            self.path.set(self.img_path)
        except:
            self.path.set('please select a image!')

    def resize(self, pil_image):
        w, h = pil_image.size
        f1 = 1.0*self.main_w/w
        f2 = 1.0*self.main_h/h
        factor = min([f1, f2])
        width = int(w*factor)
        height = int(h*factor)
        print(factor)
        return pil_image.resize((width, height), Image.ANTIALIAS)

    def show_image(self):
        src_image = Image.open(self.img_path)
        resized_image = self.resize(src_image);
        self.tk_image = ImageTk.PhotoImage(image=resized_image)
        self.label = tk.Label(self, image=self.tk_image)
        self.label.grid(row=2,column=0,columnspan=2)

    def img_split(self):
        imsplit(self.img_path, 3, 1)

def mainApp(w, h):
    root = tk.Tk()
    root.geometry('{0}x{1}+400+200'.format(w, h))
    root.title('图片切割程序')
    #root.overrideredirect(1)
    root.iconbitmap('icon.ico')
    app = App(root)
    root.mainloop()

if __name__ == '__main__':
    # imsplit('./20200204080200.jpg', 3, 1);
    mainApp(main_w, main_h)
