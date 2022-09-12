n = int(input())
a = [int(i) for i in input().split()]
res = 1
mx = -1999999
cnt = 0
for i in range (0, n):
    if(a[i] > mx):
        mx = a[i]
for i in range (0, n):
    if(a[i] == mx):
        cnt = cnt + 1
    else:
        cnt = 0
    res = max(res, cnt)  
print(res)