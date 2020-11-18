#MLE 1

from razdel3.read import x1

def C(n, k):
    if 0 <= k <= n:
        nn = 1
        kk = 1
        for t in range(1, min(k,  n - k) + 1):
            nn *= n
            kk *= t
            n -= 1
        return nn // kk
    else:
        return 0


def binom_P(k,n,p):
    res = 1
    res = res * C(n,k) * (p**k) * ((1-p)**(n-k))
    return res

k = sum(x1)
n = len(x1)
print("Логарифм фукнции правдоподобия: ln L = ln C(n,k) + k * ln p + (n-k) * ln(1-p)")
print("Оценка для параметра p: k/n")
print(f"Вычисленное значение p для данной выборки при помощи полученной оценки: {k/n}")
p1 = 0.4
p2 = 0.5
p3 = 0.6

# print(binom_P(k,n,p1))
# print(binom_P(k,n,p2))
# print(binom_P(k,n,p3))