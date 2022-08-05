def check_tn(a):
    if a == a[::-1] and len(a) > 1:
        return 1
    return 0

def solve():
    n, m = map(int, input().split())
    L = []
    maxx = -1
    for i in range(n):
        a = []
        for j in input().split():
            a.append(int(j))
            if check_tn(j) and maxx < int(j):
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