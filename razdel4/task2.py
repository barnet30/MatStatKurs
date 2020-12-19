import pandas as pd
from razdel4.read_csv import df2
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
y=81

def estimate_coef(x,y):
    n = np.size(x)
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    var_x = np.var(x)
    var_y = np.var(y)
    std_err_x = var_x**0.5
    std_err_y = var_y**0.5
    r = sum([(x[i] - mean_x) * (y[i] - mean_y) for i in range(n)]) / n / (std_err_x * std_err_y)
    b = r * std_err_x / std_err_y
    b0 = mean_x - mean_y * b
    b1 = b
    return [b0,b1]


#a, b, corr, p_value,std_err = stats.linregress(df2['Y'],df2['X'])
#print(corr,std_err)
coeff = estimate_coef(df2['X'], df2['Y'])
a = coeff[1]
b = coeff[0]
x_reg = df2['Y']*a + b
x_predict = a*y+b

# print(a,b)
# print(coeff[1],coeff[0])


plt.scatter(df2['X'],df2['Y'],color="red",marker="o")
# plt.plot([x_predict,x_predict],[0,y],color="blue")
# plt.plot([0,x_predict],[y,y],color="blue")
plt.plot(x_reg,df2['Y'],color="green",label=f"x={a}*Y+{b}")
plt.legend()
plt.show()

print(x_predict)

