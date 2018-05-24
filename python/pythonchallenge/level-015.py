#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2018-05-24 16:08:04
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : level 15 of python challenge
# 
# 思路：这一关页面上只有一张图片，图片上是两只猫，看起来这个图片是上一关中第二幅图的完整版本
#       网页标题uzi，并且附带一句描述and its name is uzi. you'll hear from him later.
#       打开网页源码也没有找到更有意义的线索，看来必须了解一下uzi是什么东西，现上网查一下吧
#       没有看到任何与Python有关的内容，还是参考一下别人的吧
#       
#       请无视上面的内容，出现上面的分析完全是因为第14关我以为做完了，实际上并没有，真正的15关在下面
#       
#       这一关同样是一幅图，图片中的内容貌似一个日历，日历显示January 1*6，数字1和6之间有一个孔
#       其中26号被笔圈起来了，网页标题是whom?，源码中有两句提示<!-- he ain't the youngest, he is the second -->
#       和<!-- todo: buy flowers for tomorrow -->貌似是根据线索猜一个人，可这跟Python有什么关系，他并不是最年轻，是第二名
#       ，为明天献花！！！这些线索我真的猜不出是谁...
#       补充一下漏掉的线索，看日历下方的小日历发现2月份是29天，所以这个是一个闰年，然后这一天是周一，1*6应该代表的是1XX6年
#       再根据he ain't the youngest, he is the second，在所有的记过中选择第二年轻的日期，它是1756-01-26，然后buy flowers for tomorrow
#       表明1月27日是一个人的生日（这我真的猜不到），即使知道1756-01-27是一个人的生日，我也不知道它是谁，大神给出的是Mozart，
#       那下一关url就是mozart
#       
#       我又查了一下，Mozart原来是莫扎特，这我上哪知道去！！！
# 
# 备注：1. python challenge home page : http://www.pythonchallenge.com/
#       2. current level url : http://www.pythonchallenge.com/pc/return/cat.html
#       3. next level url : http://www.pythonchallenge.com/pc/return/mozart.html
#       4. username:huge password:file
#

import datetime
import calendar

def main():
    for year in range(1006, 1996, 10):
        date = datetime.date(year, 1, 26)
        if calendar.isleap(year) and date.isoweekday() == 1:
            print(date)

if __name__ == '__main__':
    main()

# 运行结果，选第2大的日期加1天就是Mozart的生日（1756-01-27）
'''
1176-01-26
1356-01-26
1576-01-26
1756-01-26
1976-01-26
[Finished in 0.1s]
'''