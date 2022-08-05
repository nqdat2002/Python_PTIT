import math


n = int(input())
num =  int(math.sqrt(n)) + 1

f = [1] * num
L = []
def sang():
    f[0] = 0
    f[1] = 0

    for i in range(2, num):
        if f[i] == 0:
            continue
        L.append(i)
        for j in range(i * i, num, i):
            f[j] = 0

sang()

res = 0
for i in L:
    tmp = i ** 8
    if tmp > n:
        break
    res += 1

for i in range(len(L)):
    if i ** 2 > n: break
    for j in range(i + 1, len(L)):
        if (L[i] * L[j]) ** 2 <= n:
            res += 1
        else:
            break

print(res)
