def Eratosthens():
    f = [1] * 1001
    f[0] = 0
    f[1] = 0
    for i in range (2, 1001):
        if f[i] == 0:
            continue
        for j in range(i * i, 1001, i):
            f[j] = 0
    return f

n, m = map(int, input().split())
f = Eratosthens()
for i in range(n):
    for j in input().split():
        print (f[int(j)], end = ' ')
    print()

