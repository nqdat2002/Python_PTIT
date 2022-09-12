ktra = [1] * 1001
def sang():
    ktra[0] = 0
    ktra[1] = 0
    for i in range(2, 1001):
        if ktra[i] == 0:
            continue
        for j in range(i * i, 1001, i):
            ktra[j] = 0

sang()
n = int(input())
L = []
ngto = []
for i in input().split():
    a = int(i)
    L.append(a)
    if ktra[a] == 1:
        ngto.append(a)
ngto.sort()

j = 0
for i in L:
    if ktra[i] == 0:
        print(i, end = ' ')
    else:
        print(ngto[j], end = ' ')
        j += 1