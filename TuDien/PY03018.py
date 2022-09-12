from random import randrange


a = []
b = []
oo = 100000
for i in range(1005):
    c = []
    for j in range (1005):
        c.append(0)
    a.append(c)
    b.append(c)
t = int(input())
def Solve(n, m):
    r = []
    r.append((1, 1))
    b[1][1] = 0
    while len(r) > 0:
        x = r[0][0]
        y = r[0][1]
        r.pop(0)
        if x == n and y == m:
            print(b[x][y])
            return
        if x + 1 <= n:
            i = x + abs(a[x][y] - a[x + 1][y])
            j = y
            if i <= n and b[i][j] == oo:
                b[i][j] = b[x][y] + 1;
                r.append((i, j))
        if y + 1 <= m:
            i = x
            j = y + abs(a[x][y] - a[x][y + 1])
            if j <= m and b[i][j] == oo:
                b[i][j] = b[x][y] + 1;
                r.append((i, j))
        i = x + abs(a[x][y] - a[x + 1][y + 1])
        j = y + abs(a[x][y] - a[x + 1][y + 1])
        if i <= n and j <= m and b[i][j] == oo:
            b[i][j] = b[x][y] + 1
            r.append((i, j))
    print(-1)
        
while t > 0:
    n, m = map(int, input().split())
    for i in range(1, n + 1):
        a[i] = [int(x) for x in input().split()]
    