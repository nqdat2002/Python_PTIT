n = int(input())
tren, duoi = 0, 0
for i in range(0, n):
    a = [int(i) for i in input().split()]
    for j in range(0, n):
        if j > n - i - 1:
            duoi += a[j]
        elif j < n - i - 1:
            tren += a[j]
k = int(input())
ans = abs(tren - duoi)
if ans <= k:
    print("YES")
else:
    print("NO")
print(ans)