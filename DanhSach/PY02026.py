n, m = map(int, input().split())
f = [0] * 1001
dem = 0
for i in input().split():
    if f[int(i)] == 0:
        f[int(i)] = 1
        dem += 1

f1 = [0] * 1001
for i in input().split():
    if f[int(i)] == 0:
        dem = -1
        break
    else:
        if f1[int(i)] == 0:
            dem -= 1
        f1[int(i)] = 1

if dem == 0:
    print("YES")
else:
    print("NO")