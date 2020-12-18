from razdel4.read_csv import df1
from math import inf
import numpy as np
from scipy import stats
import pandas as pd
alf = 0.05
r = 4
s = 6

def calc_n_i_j(i,j):
    x1 = x_split[i-1]
    x2=x_split[i]
    y1=y_split[j-1]
    y2=y_split[j]
    return df1[(df1['X']<x2) & (df1['X']>x1) & (df1['Y']<y2)  & (df1['Y']>y1)]

n = len(df1['X'])
x_split = [-inf,118.05,120.7167,123.3833,126.05,inf]
y_split = [-inf,80.05,81.25,82.45,83.65,84.85,86.05,inf]

n_con = np.array([[len(calc_n_i_j(i,j)) for j in range(1,s+2)] for i in range(1,r+2)])
nX = np.array([sum(s) for s in n_con])
nInv = n_con.transpose()
nY = np.array([sum(s) for s in nInv])
n_con = np.vstack([n_con,nY])
nX = np.append(nX,len(df1['X']))

n_df_con = pd.DataFrame(n_con,columns=['B1','B2','B3','B4','B5','B6','B7'],index=['A1','A2','A3','A4','A5','nY'])


print(n_con)
print(nX)
print(nY)




n_df_con['nX'] = nX

T=0
for i in range(r+1):
    for m in range(s+1):
        T+=((n*n_con[i][m] - nX[i]*nY[m])**2) / (n*nX[i]*nY[m])
print('--------------')
print(n_df_con)

print(f"Уровень значимости = {alf}")

print(f"Статистика T = {T}")


critical = stats.chi2.ppf(1-alf,r*s)
#print(f"critical = {critical}")
p_value = 1 - stats.chi2.cdf(T,r*s)
print(f"Критический уровень значимости (p-value) = {p_value}")
if p_value > alf:
    print("H0 принимается")
else:
    print("H0 отклоняется")