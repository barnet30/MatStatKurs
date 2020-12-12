#MLE 1
import pandas as pd
from functools import reduce

data = pd.read_csv('r3z1.csv')

def estimate(X):
    return sum(X)/len(X)


def f(x,p):
    return p*x + (1-p)*(1-x)

def L(X,p):
    return (reduce(lambda x,y: x*y, [f(x, p) for x in X]),p)

print(f"Oценка: {estimate(data['X'])}")

TETA = [0.4,0.5,0.6]

for teta in TETA:
    print(L(data["X"],teta))

