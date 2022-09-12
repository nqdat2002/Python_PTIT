f = [0] * 42
n = 0
while True:
    s = input().split()
    for i in s:
        f[int(i) % 42] += 1
    n += len(s)
    if n == 10:
        break

res = 0

for i in f:
    if i > 0:
        res += 1
print(res)