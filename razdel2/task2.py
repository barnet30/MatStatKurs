import matplotlib.pyplot as plt
from razdel2.read_csv import sample
import collections
import math

alf = 0.05
l = 1.5      # Лямбда для показательного распределения
eps = 1e-15

#функция показательного распределения
def eps_fr(l,x):
    return (1 - math.exp(-l*x))

def kolm_quantil():
    return math.sqrt((-1/2)*(math.log(alf/2)))


def graph_EFR(sample):

    plt.plot(x, y)
    plt.suptitle('Эмпирическая функция распределения')
    plt.xlabel('X')
    plt.ylabel('F(X)')

    plt.plot(sorted(sample), [eps_fr(l,x) for x in sorted(sample)], color= 'green',lw = 4)
    plt.xlabel('X')
    plt.ylabel('E(X)')
    plt.show()

distribution = sorted(collections.Counter(sample).most_common(), key=lambda elem: elem[0])

x = []
y = []
sum_for_y = 0
for pair in distribution:
    if pair != distribution[0]:
        x.append(prev[0])
        y.append(sum_for_y/len(sample))
    x.append(pair[0])
    y.append(sum_for_y/len(sample))
    prev = pair
    sum_for_y += pair[1]

#graph_EFR(sample)

D_n = max(max([math.fabs(y[i] - eps_fr(l,y[i])) for i in range(len(y))]),
          max([math.fabs((y[i]+eps) - eps_fr(l,y[i]+eps)) for i in range(len(y))]))
statistic = D_n * math.sqrt(len(sample))
k_quantil = kolm_quantil()

p_value = eps_fr(l,statistic)

print(f"Критическая константа = {k_quantil}")
print(f"Статистика = {statistic}")

if statistic > k_quantil:
   print("Гипотеза отклоняется")
else:
    print("Гипотеза принимается")

print(f"P-value = {p_value}")