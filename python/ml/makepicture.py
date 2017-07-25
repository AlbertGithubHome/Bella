#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#a test for making picture


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)


dates = pd.date_range('2017-07-22', periods = 6)
print(dates)

df = pd.DataFrame(np.random.randn(6,4), index = dates, columns = list('ABCD'))
print(df)
print(df.dtypes)
#print(df.<TAB>)
print(df.head())
print(df.tail(2))
print(df.index)
print(df.columns)
print(df.values)
print(df.describe())

print(df.T)

plt.figure();
plt.plot(df); 
plt.legend(loc='best')
plt.show()
#ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
#ts = ts.cumsum()
#print(ts)
#ts.plot()