n = int(input())
tren, duoi = 0, 0
for i in range(0, n):
    a = [int(i) for i in input().split()]
    for j in range(0, n):
        if j < i:
            duoi += a[j]
        elif j > i:
            tren += a[j]
k = int(input())
ans = abs(tren - duoi)
if ans <= k:
    print("YES")
else:
    print("NO")
print(ans)