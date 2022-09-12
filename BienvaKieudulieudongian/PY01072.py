

n, k = map(int, input().split())

set1 = set([int(i) for i in input().split()])
L = sorted(set1)
n = len(L)
s = []
for i in range(0, k + 1):
    s.append(i)

while True:
    for i in range(1, len(s)):
        print(L[s[i] - 1], end = ' ')
    print()
    i = k
    while s[i] == n - k + i: i -= 1
    if i < 1: break
    s[i] += 1
    for j in range(i + 1, k + 1):
        s[j] = s[j - 1] + 1
