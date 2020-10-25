# Гипотеза H0: выборка имеет показательное распредление с параметром lambda = 1.5
import matplotlib.pyplot as plt
from razdel2.read_csv import sample
import numpy as np
import collections
import math
from scipy.special import kolmogorov


alf = 0.05
l = 1.5      # Лямбда для показательного распределения
eps = 1e-15

#эмпирическая функция распределения
def efr(sample):
    sample = np.sort(sample)
    def result(x):
        return np.searchsorted(sample, x, side='right') / sample.size
    return result


#функция показательного распределения
def exp_fr(l,x):
    return (1 - math.exp(-l*x))

# (1-альфа) - квантиль
def kolm_quantil(quant):
    return math.sqrt((-1/2)*(math.log(quant/2)))

#функция распредления Колмогорова
def kolm_fr(x):
    return (1 - 2 * (math.exp(-2*(x*x))))

#построение эфр выборки с наложением функции показательного распределения
def graph(sample):
    x = []
    y = []
    sum_for_y = 0
    for pair in distribution:
        if pair != distribution[0]:
            x.append(prev[0])
            y.append(sum_for_y / len(sample))
        x.append(pair[0])
        y.append(sum_for_y / len(sample))
        prev = pair
        sum_for_y += pair[1]
    
    plt.plot(x, y)
    plt.suptitle('Эмпирическая функция распределения')
    plt.xlabel('X')
    plt.ylabel('F(X)')

    plt.plot(sorted(sample), [exp_fr(l,x) for x in sorted(sample)], color= 'green',lw = 4)
    plt.xlabel('X')
    plt.ylabel('E(X)')
    plt.show()

distribution = sorted(collections.Counter(sample).most_common(), key=lambda elem: elem[0])

cdf = efr(sample)


graph(sample)

D_n = max(max([math.fabs(cdf(val) - exp_fr(l,val)) for val in sample]),
          max([math.fabs(cdf(val+eps) - exp_fr(l,val+eps)) for val in sample]))
statistic = D_n * math.sqrt(len(sample))
k_quantil = kolm_quantil(alf)

p_value = kolmogorov(statistic)

print(f"Критическая область имеет вид: Statistic > {k_quantil}")
print(f"Критическая константа = {k_quantil}")
print(f"Статистика = {statistic}")

if statistic > k_quantil:
   print("Гипотеза отклоняется")
else:
    print("Гипотеза принимается")

print(f"P-value = {p_value}")








# from scipy import stats
# first = sample
# second = [exp_fr(l,value) for value in sample]
#
# print(stats.ks_2samp(first,second))