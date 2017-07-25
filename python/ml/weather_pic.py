#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#a test for making plain picture


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

list_min = [22, 20, 22, 22, 21, 22, 23]
list_max = [25, 24, 28, 29, 30, 31, 32]

dates = pd.date_range('2017-07-26', periods = 7)
plt.plot(dates, list_min, ".-", label='min Degree', color='b')
plt.plot(dates, list_max, ".-", label='max Degree', color='r')
plt.legend()
plt.show()
