road = {}
check = {}
mark = {}

def init():
    for i in range(1,n+1):
        check[i] = 0
        mark[i] = 1

def findSimilar():
    for i in range(1,n+1):
        if check[i] == 1 and mark[i] == 1:
            mark[i] = 1
        else:
            mark[i] = 0

def DQQL(r,end):
    if r == end:
        findSimilar()
    else:
        for i in range(len(road[r])):
            v = road[r][i]
            if check[v] == 0:
                check[v] = 1
                DQQL(v,end)
                check[v] = 0

for i in range(int(input())):
    n, m, u, v = [int(i) for i in input().split()]
    for i in range(m):
        a, b = [int(i) for i in input().split()]
        if a in road:
            road[a].append(b)
        else:
            road[a] = [b]
    init()
    DQQL(u,v)
    check[u] = 1
    count = 0
    for i in range(1,n+1):
        if i!=u and i!=v and mark[i]==1:
            count += 1
    print(count)
    for i in road:
        road[i].clear()