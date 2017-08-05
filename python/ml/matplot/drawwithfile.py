#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#a test for drawing a plot with data file

__author__ = 'AlbertS'

import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('data/plotdata.txt', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=' ')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x, y, label='load data from file')
plt.xlabel('x')
plt.ylabel('y')

plt.title('Data from file')
plt.legend()
plt.show()