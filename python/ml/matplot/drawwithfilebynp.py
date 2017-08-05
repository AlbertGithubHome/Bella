#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#a test for drawing a plot with data file by numpy

__author__ = 'AlbertS'

import matplotlib.pyplot as plt
import numpy as np

x, y = np.loadtxt('data/plotdata.txt', delimiter=' ', unpack=True)
plt.plot(x, y, label='load data from file')
plt.xlabel('x')
plt.ylabel('y')

plt.title('Data from file')
plt.legend()
plt.show()