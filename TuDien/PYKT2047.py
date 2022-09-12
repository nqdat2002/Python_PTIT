def Lower_Bound(a, n, k):
    l, r = 1, n
    while l < r:
        m = (l + r) >> 1
        if k <= a[m]:
            r = m;
        else:
            l = m + 1
    if l <= n - 1 and a[l] < k:
        l += 1
    return l

t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    s = []
    for i in range(n + 1): s.append(0)
    l = []
    l.append(0)
    ll = [int(x) for x in input().split()]
    h = []
    h.append(0)
    hh = [int(x) for x in input().split()]
    for i in range (1, n + 1):
        l.append(ll[i - 1])
        h.append(hh[i - 1])
    for i in range (1, n + 1):
        if i == 1:
            s[i] = h[i] * l[i]
        else:
            if h[i] > h[i - 1]:
                tru = 0
                tmp = i - 1
                while h[i] > h[tmp] and tmp > 0:
                    tru += h[tmp]
                    tmp -= 1
                if tmp != 0:
                    s[i] = s[tmp] + h[i] * (l[i] - l[tmp] - 1) - tru
                else:
                    s[i] = h[i] * l[i] - tru
            else:
                s[i] = s[i - 1] + h[i] * (l[i] - l[i - 1] - 1)

    q = int(input())
    while q > 0:
        q -= 1
        k = int(input())
        res = Lower_Bound(s, n, k)
        print(res - 1)
        