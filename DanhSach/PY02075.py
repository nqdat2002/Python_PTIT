t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    a = [1] * n
    b = [1] * n
    r = []
    res = 1
    index = 0
    for i in range (n):
        a[i], b[i] = map(int, input().split())
    for i in range (n):
        r.append((a[i],b[i]))
    r.sort(key = lambda x: x[1])
    for i in range (1, n):
        if r[i][0] >= r[index][1]:
            res += 1
            index = i
    print(res)
    