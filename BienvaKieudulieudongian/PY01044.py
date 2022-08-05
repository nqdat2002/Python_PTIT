s1 = set(input().lower().split())
s2 = set(input().lower().split())

res1 = s1|s2
res2 = s1&s2

res1 = sorted(res1)
res2 = sorted(res2)

for i in res1:
    print(i, end = ' ')
print()

for i in res2:
    print(i, end = ' ')
print()