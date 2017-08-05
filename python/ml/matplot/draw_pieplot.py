#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#a test for drawing a pie plot

__author__ = 'AlbertS'

import matplotlib.pyplot as plt

slicesdata = [7,3,10,4]
activities = ['sleeping', 'eating', 'working', 'playing']
colors = ['m', 'g', 'r', 'b']

plt.pie(slicesdata, labels=activities, startangle=90, shadow=True, explode=(0, 0.1, 0, 0), autopct='%1.1f%%')
plt.title('Pie Plot!')
plt.show()
