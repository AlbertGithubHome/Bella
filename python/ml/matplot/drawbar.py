#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#a test for drawing a bar

__author__ = 'AlbertS'

import matplotlib.pyplot as plt


plt.bar([1,3,5,7,9], [23,21,54,13,87], label="line one")
plt.bar([2,4,6,8,10], [3,61,44,16,57], label="line two")
plt.legend()

plt.xlabel('bar number')
plt.ylabel('bar value')

plt.title('This A Bar Graph!')

plt.show()


