def Eratosthens():
    f = [1] * 7950
    f[0] = 0
    f[1] = 0
    for i in range (2, 7950):
        if f[i] == 0:
            continue
        for j in range(i * i, 7950, i):
            f[j] = 0
    ans = []
    for i in range(2, 7950):
        if f[i] == 1:
            ans.append(i)
    return ans

n, x = map(int, input().split())
f = Eratosthens()
for i in range(n + 1):
    print(x, end = ' ')
    x += f[i]

