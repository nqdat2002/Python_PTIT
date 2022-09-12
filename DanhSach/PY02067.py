n = int(input())
a = [int(i) for i in input().split()]

m = 100000
res = 0
for i in range (0, n):
    m = min(m, a[i])
    
for i in range(m, 0, -1):
    x = True
    for j in range(0, n):
        r = a[j] // i
        if a[j] // r == i:
            while r > 0 and a[j] // r == i:
                r = r - 1
            res = res + (r + 1)
        else:
            res = 0
            x = False
            break    
    if x == True:
        print(res)
        break