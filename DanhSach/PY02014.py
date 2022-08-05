check = []

def sang():
    f = [1] * 10010
    f[0] = 0
    f[1] = 0
    for i in range(2, 10010):
        if f[i] == 0: continue
        if i * i > 10008: break
        for j in range(i*i, 10010, i):
            f[j] = 0
    for i in range(2, 10010):
        if f[i] == 1:
            check.append(i)
    del f

def lowerBound(l, r, value):
    res = -1
    while l <= r:
        mid = int ((l + r) / 2)
        if check[mid] > value:
            r = mid - 1
        else:
            res = mid
            l = mid + 1
    return res

def solve():
    sang()
    n = input()
    L = [int(i) for i in input().split()]
    res = -1
    for i in L:
        tmp = lowerBound(0, len(check), i)
        if tmp == -1:
            tmp += 1
            res = max(res, check[tmp] - i)
        else:
            res = max(res, min(i - check[tmp], check[tmp + 1] - i))
    print(res)
solve()

