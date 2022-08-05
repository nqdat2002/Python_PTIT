t = int(input())
while t > 0:
    t -= 1
    n, m = map(int, input().split())
    m %= n
    a = [int(i) for i in input().split()]
    for i in range(m, n):
        print(a[i], end=" ")
    for i in range(0, m):
        print(a[i], end=" ")
    print()