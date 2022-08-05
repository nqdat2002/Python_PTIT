f = [1] * 1001

def sang():
    f[0] = 0
    f[1] = 0
    for i in range(2, 1001):
        if f[i] == 0:
            continue
        if i * i > 1000: 
            break
        for j in range(i * i, 1001, i):
            f[j] = 0

def solve():
    n, m = map(int, input().split())
    L = []
    sang()
    maxx = -1
    for i in range(n):
        a = []
        for j in input().split():
            a.append(int(j))
            if f[int(j)] and maxx < int(j):
                maxx = int(j)
        L.append(a)
    dd = 1
    arr = []
    
    for i in range(n):
        for j in range (m):
            if L[i][j] == maxx:
                arr.append([i, j])
                dd = 0
    if dd == 1:
        print("NOT FOUND")
        return
        
    print(maxx)
    for i in arr:
        print("Vi tri [" + str(i[0]) + "][" + str(i[1]) + ']')
solve()