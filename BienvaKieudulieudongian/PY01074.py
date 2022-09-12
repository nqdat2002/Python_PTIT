import math as mt
 
MAXN = 2000001
spf = [0 for i in range(MAXN)]
def sieve():
    spf[1] = 1
    for i in range(2, MAXN):
        spf[i] = i
    for i in range(4, MAXN, 2):
        spf[i] = 2
    for i in range(3, mt.ceil(mt.sqrt(MAXN))):
        if (spf[i] == i):
            for j in range(i * i, MAXN, i):
                if (spf[j] == j):
                    spf[j] = i

t = int(input())
res = 0
# sieve()
# cnt = 0
# for i in range(len(spf)):
#     print(spf[i], end = ', ')

while t > 0:
    t -= 1
    n = int(input())
    while n != 1:
        res += spf[n]
        n = n // spf[n]
print(res)