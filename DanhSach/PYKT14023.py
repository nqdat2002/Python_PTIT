a = [0] * 100005

def update(id, l, r, x, y):
    if x > r or y < l:
        return
    if l == r:
        if a[id] == 0:
            a[id] = 1
        else:
            a[id] = 0
        return
    m = (l + r) >> 1
    update(id * 2, l, m, x, y)
    update(id * 2 + 1, m + 1, r, x , y)

n, q = map(int, input().split())
while q > 0:
    q -= 1
    l, r = map(int, input().split())
    a[l] += 1
    a[r + 1] -= 1
for i in range (2, n + 1):
    a[i] += a[i - 1]
for i in range (1, n + 1):
    if a[i] % 2 == 0:
        print(0, end = " ")
    else:
        print(1, end = " ")
    