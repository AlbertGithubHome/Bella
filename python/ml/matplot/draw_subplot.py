#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#a test for drawing a surface

__author__ = 'AlbertS'

import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X = [1, 1, 2, 2, 2]
Y = [3, 4, 4, 3, 4]
Z = [1, 2, 1, 1, 2]
ax.plot_trisurf(X, Y, Z)
plt.show()