cnt = 0
def Try(i, s1, s2, sum, a, n):
    global cnt
    if s1 > sum // 3 or s2 > sum // 3:
        return
    if sum - s1 - s2 == sum // 3:
        cnt += 1
        return
    for j in range(i + 1, n):
        Try(j, s1 + a[j], s2, sum, a, n)
        Try(j, s1, s2 + a[j], sum, a, n)

t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    m = [int(x) for x in input().split()]
    sum = 0
    for i in range(n): sum += m[i]
    if sum % 3 != 0:
        print(0)
        continue
    Try(-1, 0, 0, sum, m, n)
    print(cnt)
    cnt = 0