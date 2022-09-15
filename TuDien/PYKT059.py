def dfs(u):
    dd[u] = 1
    for v in ke[u]:
        if dd[v] == 0:
            dfs(v)
    pass

test = 1
for t in range(test):
    n, m, x = map(int, input().split())
    ke = [[] for i in range(n + 1)]
    for i in range(m):
        u, v = map(int, input().split())
        ke[u].append(v)
        ke[v].append(u)
    dd = [0 for i in range(n + 1)]
    cnt = [0 for i in range(n + 1)]
    tmp = 0
    for i in range(1, n + 1):
        if dd[i] == 0:
            dfs(i)
            tmp += 1
            for j in range(1, n + 1):
                if dd[j] == 1 and cnt[j] == 0:
                    cnt[j] = tmp
    for i in range(1, n + 1):
        if cnt[i] != cnt[x]:
            print(i)
