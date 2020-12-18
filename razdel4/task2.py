import pandas as pd
from razdel4.read_csv import df2
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
y=81

plt.scatter(df2['X'],df2['Y'],color="red",marker="o")

a, b, corr, p_value,std_err = stats.linregress(df2['Y'],df2['X'])
x_reg = df2['Y']*a + b
x_predict = a*y+b
print(corr,std_err)
# plt.plot([x_predict,x_predict],[0,y],color="blue")
# plt.plot([0,x_predict],[y,y],color="blue")
plt.plot(x_reg,df2['Y'],color="green",label=f"x={a}*Y+{b}")
plt.legend()
plt.show()

print(x_predict)

