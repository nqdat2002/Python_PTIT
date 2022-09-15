def dfs(u):
    dd[u] = 1
    for v in ke2[u]:
        if v != 0 and dd[v] == 0:
            dfs(v)
    pass

test = int(input())
for t in range(test):
    n, m = map(int, input().split())
    ke = [[] for i in range(n + 1)]
    ke2 = [[] for i in range(n + 1)]
    for i in range(m):
        u, v = map(int, input().split())
        ke[u].append(v)
        ke[v].append(u)
        ke2[u].append(v)
        ke2[v].append(u)
    dd = [0 for i in range(n + 1)]
    for j in range(len(ke2[1])):
        ke2[1][j] = 0
    for i in range(2, n + 1):
        for j in range(len(ke2[i])):
            if ke2[i][j] == 1:
                ke2[i][j] = 0
    ans = 0
    tmp = 0
    pos = 0
    for i in range(2, n + 1):
        if dd[i] == 0:
            tmp += 1
            dfs(i)
    if ans < tmp:
        ans = tmp
        pos = 1
    for j in range(len(ke2[1])):
        ke2[1][j] = ke[1][j]
    for i in range(2, n + 1):
        for j in range(len(ke2[i])):
            if ke2[i][j] == 0:
                ke2[i][j] = 1
    #print(tmp)
    for i in range(2, n + 1):
        tmp = 0
        dd = [0 for i in range(n + 1)]
        for j in range(len(ke2[i])):
            ke2[i][j] = 0
        for j in range(1, n + 1):
            if j != i:
                for k in range(len(ke2[j])):
                    if ke2[j][k] == i:
                        ke2[j][k] = 0
        #print(ke2)
        for j in range(1, n + 1):
            if j != i and dd[j] == 0:
                tmp += 1
                dfs(j)
        if ans < tmp:
            ans = tmp
            pos = i
        for j in range(len(ke2[i])):
            ke2[i][j] = ke[i][j]
        for j in range(1, n + 1):
            if j != i:
                for k in range(len(ke2[j])):
                    if ke2[j][k] == 0:
                        ke2[j][k] = i
        #print(ke2)
        #print(tmp)
    if ans == 1:
        pos = 0
    print(pos)