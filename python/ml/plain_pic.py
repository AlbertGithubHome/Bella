#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#a test for making plain picture


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def make_pic():
    dates = pd.date_range('2017-07-22', periods = 6)
    df = pd.DataFrame(np.random.randn(6,4), index = dates, columns = list('ABCD'))
    plt.plot(df, "-", label='a')
    plt.legend()
    plt.show()

def make_pic_with_column():
    dates = pd.date_range('2017-07-22', periods = 6)
    df = pd.DataFrame(np.random.randn(6,4), index = dates, columns = list('ABCD'))
    df.plot()
    plt.show()

if __name__ == "__main__":
    make_pic_with_column()