#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#a test for drawing a senior bar
#按照区间段分组

__author__ = 'AlbertS'

import matplotlib.pyplot as plt

all_ages = [1,32,43,54,64,76,23,19,34,21,65,87,12,5,6,2,12,21,72,12,7,12,78,23,91,2,17,63,11,55,120,112,103,110]
segments = [0,10,20,30,40,50,60,70,80,90,100,110,120]

plt.hist(all_ages, segments, histtype='bar', rwidth=0.5)
plt.xlabel('x')
plt.ylabel('count')

plt.title('Senior Bar!')
plt.legend()
plt.show()

