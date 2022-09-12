n, k = map(int, input().split())
a = [int(i) for i in input().split()]
cnt = 0
a.sort()
for i in range(0, n - 1):
    if(a[i + 1] - a[i] > k):
        cnt = cnt + 1
print(cnt + 1)