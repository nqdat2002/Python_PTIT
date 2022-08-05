def solve():
    n, m = map(int, input().split())
    L = []
    minn = -1
    maxx = -1
    for i in range(n):
        a = []
        for j in input().split():
            a.append(int(j))
            if minn == -1 or minn > int(j):
                minn = int(j)
                continue
            if maxx == -1 or maxx < int(j):
                maxx = int(j)
                continue
        L.append(a)
    dd = 1
    arr = []
    
    for i in range(n):
        for j in range (m):
            if L[i][j] == maxx - minn:
                arr.append([i, j])
                dd = 0
    if dd == 1:
        print("NOT FOUND")
        return
        
    print(maxx - minn)
    for i in arr:
        print("Vi tri [" + str(i[0]) + "][" + str(i[1]) + ']')
solve()