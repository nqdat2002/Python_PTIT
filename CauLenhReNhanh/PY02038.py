n = int(input())
L = []
res = 0
for i in range(n):
    s = input()
    a = []
    dem = 0
    for j in s:
        if j == 'C':
            a.append(1)
            dem += 1
        else:
            a.append(0)
    L.append(a)
    res += int((dem * (dem - 1)) / 2)

for j in range(n):
    dem = 0
    for i in range(n):
        dem += L[i][j]
    res += int((dem * (dem - 1)) / 2)

print(res)