def show(ans):
    for i in ans:
        for j in i:
            print(j, end = ' ')
        print()

def rotate(n, m, L):
    Arr = []
    for i in range(m):
        a = []
        for j in range(n):
            a.append(L[j][i])
        Arr.append(a)
    return m, n, Arr

def bienDoi(bd, n, m, L):
    if bd == 1:
        n, m, L = rotate(n, m, L)
    f = [0] * n
    dem = 0
    for i in range(bd, n, 2):
        dem += 1
        f[i] = 1
        if n - dem == m:
            break
    for i in range(n - 1, -1, -1):
        if f[i]:
            del L[i]
    del f[i]
    n = len(L)

    if bd == 1:
        n, m, L = rotate(n, m, L)
    return (L, n, m)


def solve():
    n, m = map(int, input().split())

    L = []
    for i in range(n):
        a = []
        for j in input().split():
            a.append(int(j))
        L.append(a)

    while n != m:
        if n > m:
            L, n, m = bienDoi(0, n, m, L)
        else:
            L, n, m = bienDoi(1, n, m, L)
    show(L)
solve()