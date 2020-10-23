import matplotlib.pyplot as plt
from razdel2.read_csv import sample
import collections
import numpy as np
import math

alf = 0.05
l = 1.5      # Лямбда для показательного распределения


def eps_fr(l,x):
    return (1 - math.exp(-l*x))

def graph_EFR(sample):
    distribution = sorted(collections.Counter(sample).most_common(), key=lambda elem: elem[0])

    x = []
    y = []
    sum_for_y = 0
    for pair in distribution:
        if pair != distribution[0]:
            x.append(previous[0])
            y.append(sum_for_y/len(sample))
        x.append(pair[0])
        y.append(sum_for_y/len(sample))
        previous = pair
        sum_for_y += pair[1]

    plt.plot(x, y)
    plt.suptitle('Эмпирическая функция распределения')
    plt.xlabel('X')
    plt.ylabel('F(X)')

    plt.plot(sorted(sample), [eps_fr(l,x) for x in sorted(sample)], color= 'green',lw = 4)
    plt.xlabel('X')
    plt.ylabel('E(X)')
    plt.show()

graph_EFR(sample)