t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    m = [int(x) for x in input().split()]
    mx = m[0]
    mn = m[n - 1]
    vs = [False] * 100000
    AA = [False] * 100000
    a, b = 0, 0
    for i in range(1, n):
        if m[i] >= m[0]:
            a += 1
        if m[i] > mx:
            mx = m[i]
            vs[i] = True
        else: vs[i] = False
        
    for i in range(n - 2, -1, -1):
        if m[i] < m[n - 1]:
            b += 1
        if m[i] <= mn:
            mn = m[i]
            AA[i] = True;
        else: AA[i] = False
    cnt = 0
    for i in range (1, n - 1):
        if vs[i] == True and AA[i] == True:
            cnt += 1
    if a == n - 1: cnt += 1
    if b == n - 1: cnt += 1
    print(cnt)
    