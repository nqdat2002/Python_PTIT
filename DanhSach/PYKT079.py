t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    a = [int(i) for i in input().split()]
    minn = min(a)
    maxx = max(a)
    count = 0
    for i in range(minn, maxx + 1):
        if i not in a:
            count += 1
    print(count)