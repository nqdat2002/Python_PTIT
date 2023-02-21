for t in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    cnt = 0
    for i in range(0, n - 1):
        x = max(a[i], a[i + 1])
        y = min(a[i], a[i + 1])
        while x > (y << 1):
            cnt = cnt + 1
            y <<= 1
    print(cnt)
