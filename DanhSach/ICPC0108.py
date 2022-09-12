t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    cnt = 0
    for i in range (0, n - 2):
        l = i + 1
        r = n - 1
        tmp = a[i]
        while l < r:
            if tmp + a[l] + a[r] == 0:
                cnt += 1
                l += 1
            elif tmp + a[l] + a[r] < 0:
                l += 1
            else :
                r -= 1
    print(cnt)