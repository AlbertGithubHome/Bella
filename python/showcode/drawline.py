#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2019-05-28 18:04:02
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : draw a line use python lib

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(20)
y = x * 2 + 3

plt.xlabel('x')
plt.ylabel('y')
plt.title('line')

plt.plot(x, y, ":g")
plt.show()
