#Z11;  Q = 0.975; Вид доверительной границы: Верхняя

from scipy import stats
from razdel3.read import x2

n = len(x2)
X = sum(x2)/len(x2)
Q = 0.975
alfa = 1-Q

print(f"Объём выборки: {n}")
print(f"Выборочное среднее: {X}")

sample_variance = sum([(x2[i] - X)**2 for i in range(n)]) / n
er_average = sample_variance**0.5 / ((n-1)**0.5)
print(f"Стандартная ошибка среднего: {er_average}")

q_quantil = stats.t(n-1).ppf(1-alfa)
up_limit = er_average * q_quantil + X
print(f"Верхняя доверительная граница: {up_limit}")
print(f"Доверительный интервал имеет вид: -infinity; {up_limit}")
