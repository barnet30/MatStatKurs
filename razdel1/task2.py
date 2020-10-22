import matplotlib.pyplot as plt
from razdel1.read_csv import data, sample
import collections
import seaborn

seaborn.distplot(data['X'], bins=15, color = 'blue' )
plt.suptitle('1.2 Гистограмма')
plt.xlabel('X')
plt.ylabel('Частота')
plt.show()

#print(read_csv.data['X'].value_counts())

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
plt.suptitle('1.3 Эмпирическая функция распределения')
plt.xlabel('X')
plt.ylabel('F(X)')
plt.show()