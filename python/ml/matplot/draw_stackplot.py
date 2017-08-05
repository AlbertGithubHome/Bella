#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#a test for drawing a stack plot

__author__ = 'AlbertS'

import matplotlib.pyplot as plt

days = [1,2,3,4,5,6,7]

sleeping = [10,8,6,11,10,10,12]
eating =   [2,6,4,3,6,8,10]
working =  [12,10,14,10,8,6,2]

plt.stackplot(days, sleeping, eating, working, colors=['m','b','r'])
plt.xlabel('x')
plt.ylabel('y')

plt.title('Stack Plot')
plt.title('Stack Plot')
plt.title('Stackyy Plot')
plt.show()
