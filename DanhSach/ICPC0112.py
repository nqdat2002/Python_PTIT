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
    for i in range(5, n - 5):
        if (f[i] == 1 and f[i + 2] == 1 and f[i + 6] == 1) or (f[i] == 1 and f[i + 4] and f[i + 6]):
            count += 1
    print(count)