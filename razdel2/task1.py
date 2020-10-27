# Гипотеза H1: увеличится; Гипотеза H0: не увеличится

from razdel2 import read_csv as rc

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

def binom_fr(m,n,p):
    res = 0
    for i in range(m+1):
        res += C(n,i) * (p**i) * ((1-p)**(n-i))
    return res

alf = 0.01
p0 = 0.5

z = []
for i in range(len(rc.x)):
    if rc.y[i] > rc.x[i]:
        z.append(1)
    else:
        z.append(0)

Stat_M = sum(z)

crit_const = 0
num = binom_fr(crit_const, len(z), p0)
while num < 1 - alf:
    crit_const += 1
    num = binom_fr(crit_const, len(z), p0)
crit_const -= 1

print(f"Критическая область имеет вид: M > {crit_const}")
print(f"Критическая константа = {crit_const}")
print(f"Статистика = {Stat_M}")

if Stat_M > crit_const:
    print("Гипотеза принимается")
else:
    print("Гипотеза отклоняется")

p_value = 1 - binom_fr(Stat_M, len(z), p0)
print(f"P-value = {p_value}")