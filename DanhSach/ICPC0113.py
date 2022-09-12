def Eratosthens():
    f = [1] * 1000001
    f[0] = 0
    f[1] = 0
    for i in range (2, 1000001):
        if f[i] == 0:
            continue
        for j in range(i * i, 1000001, i):
            f[j] = 0
    return f
f = Eratosthens()
t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    count = 0
    dd = {}
    for i in range(13, n):
        x = int(str(i)[::-1])
        if f[i] == 1 and i != x and f[x] == 1 and x < n and i not in dd:
            print(i, x, end=" ")
            dd[i] = 1
            dd[x] = 1
    print()