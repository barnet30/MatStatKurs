from razdel4.read_csv import df1
from math import inf
import numpy as np
alf = 0.05
r = 4
s = 6

def calc_n_i_j(i,j):
    x1 = x_split[i-1]
    x2=x_split[i]
    y1=y_split[j-1]
    y2=y_split[j]
    return df1[(df1['X']<x2) & (df1['X']>x1) & (df1['Y']<y2)  & (df1['Y']>y1)]


x_split = [-inf,118.05,120.7167,123.3833,126.05,inf]
y_split = [-inf,80.05,81.25,82.45,83.65,84.85,86.05,inf]

n = np.array([[len(calc_n_i_j(i,j)) for j in range(1,s+2)] for i in range(1,r+2)])

print(n)
