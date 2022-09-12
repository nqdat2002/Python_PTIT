def solve():
    n, m = map(int, input().split())
    L = []
    tmp = []
    ans = []
    for i in range (n):
        a = [int(i) for i in input().split()]
        L.append(a)
    for i in range (n):
        a = [0] * n
        ans.append(a)
    
    for i in range(m):
        a = [0] * n
        tmp.append(a)
        for j in range (n):
            tmp[i][j] = L[j][i]
        
    for i in range(n):
        for j in range (n):
            for k in range(m):
                ans[i][j] += L[i][k] * tmp[k][j]
    
    for i in ans:
        for j in i:
            print(j, end = ' ')
        print()

T = int(input())
while T > 0:
    solve()
    T -= 1