def dp(n, x, y, z):
    if n == 1:
        return x
    f = [0] * 10005
    f[1] = x
    for i in range(2, n + 1):
        if i % 2 == 0:
            f[i] = min(f[i - 1] + x, f[i // 2] + z)
        else:
            f[i] = min(f[i - 1] + x, f[(i + 1) // 2] + y + z)
    return f[n]

t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    x, y, z = map(int, input().split())
    res = dp(n, x, y, z)
    print(res)
    