t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    a = [0.0] * n
    b = [0.0] * n
    f = [0] * (n + 5)
    f[0] = 1
    res = 1
    for i in range (n):
        a[i], b[i] = map(float, input().split())
    for i in range (n):
        f[i] = 1
        for j in range (i):
            if a[j] < a[i] and b[j] > b[i]:
                f[i] = max(f[i], f[j] + 1)
        res = max(res, f[i])
    print(res)
    