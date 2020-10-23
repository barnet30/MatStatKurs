# Гипотеза H1: увеличится; Гипотеза H0: не увеличится

from razdel2 import read_csv as rc
# from math import factorial as fact
# import itertools

def C(n, k):
    if 0 <= k <= n:
        nn = 1
        kk = 1
        for t in range(1, min(k, n - k) + 1):
            nn *= n
            kk *= t
            n -= 1
        return nn // kk
    else:
        return 0

alf = 0.01
p0 = 0.5

z = []
for i in range(len(rc.x)):
    if rc.y[i] > rc.x[i]:
        z.append(1)
    else:
        z.append(0)

M = sum(z)

num = 0
crit_const = 0
while num < 1 - alf:
    num += C(len(z),crit_const)*(p0**len(z))
    crit_const+=1
print("Критическая константа = "+str(crit_const))

if M > crit_const:
    print("Гипотеза верна!")
else:
    print("Гипотеза неверна")

p_value = 0
for i in range(M+1):
    p_value += C(len(z),i) * (p0**len(z))
p_value = 1 - p_value
print("P-value = "+str(p_value))