#Z11;  Q = 0.975; Вид доверительной границы: Верхняя

from scipy import stats
from razdel3.read import x2

print(f"Объём выборки: {len(x2)}")
print(f"Выборочное среднее: {sum(x2)/len(x2)}")

sample_variance = sum([(x2[i] - sum(x2)/len(x2))**2 for i in range(len(x2))]) / len(x2)
er_average = sample_variance**0.5 / (len(x2)-1)**0.5
print(f"Стандартная ошибка среднего: {er_average}")
Q = 0.975
q_quantil = stats.t.ppf(Q,len(x2)-1)
up_limit = er_average * q_quantil + sum(x2)/len(x2)
print(f"Верхняя доверительная граница: {up_limit}")
print(f"Доверительный интервал имеет вид: -infinity; {up_limit}")
