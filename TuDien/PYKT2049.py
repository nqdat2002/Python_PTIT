f = [-1] * 10010

def root(u):
    if f[u] < 0:
        return u
    return root(f[u])
# DSU
q = int(input())
for k in range(q):
    x, y, z = map(int, input().split())
    if z == 1:
        x = root(x)
        y = root(y)
        if x != y:
            if f[x] > f[y]:
                t = x
                x = y
                y = t
            f[x] += f[y]
            f[y] = x
    else:
        if root(x) == root(y):
            print(1)
        else:
            print(0)
            