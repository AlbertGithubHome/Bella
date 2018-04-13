import sublime, sublime_plugin
import datetime

class PyHeadCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("insert_snippet",
            {
                "contents":"#!/usr/bin/env python3""\n"
                "# -*- coding: utf-8 -*-""\n"
                "# @Date     : ""%s" %datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") +"\n"
                "# @Author   : Albert Shi""\n"
                "# @Link     : http://blog.csdn.net/albertsh""\n"
                "# @Github   : https://github.com/AlbertGithubHome""\n"
                "__author__ = 'AlbertS'""\n"
                "# @Subject  : xxxx""\n"
                "# ""\n"
                "# 思路：xxxx""\n\n"
                # " @FileName : ""%s" %__file__ +"\n"
            }
        )

class JavaHeadCommand(sublime_plugin.TextCommand):
    def run(self,edit):
        self.view.run_command("insert_snippet",
            {
                "contents":"/**""\n"
                " * @Author:      author""\n"
                " * @Email:       xx@xx.com\n"
                " * @DateTime:    ""%s" %datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") +"\n"
                " * @Description: Description ""\n"
                " */""\n"
            }

        )
class ShHeadCommand(sublime_plugin.TextCommand):
    def run(self,edit):
        self.view.run_command("insert_snippet",
            {
                "contents":"#!/bin/sh""\n"
                "# @Author:       author""\n"
                "# @Email:        xx@xx.com\n"
                "# @DateTime:     ""%s" %datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") +"\n"
                "# @Description:  Description ""\n"
            }
        )