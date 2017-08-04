#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#a test for drawing a scatter points

__author__ = 'AlbertS'

import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9]
y = [43,21,65,87,12,21,72,12,7]

plt.scatter(x,y, label='skitscat', color='k', s=25, marker="o")

plt.xlabel('x')
plt.ylabel('count')

plt.title('Sactter Point!')
plt.legend()
plt.show()

