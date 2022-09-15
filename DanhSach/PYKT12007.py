t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    u = float(input())
    x = 1.0
    a = [float(x) for x in input().split()]
    a.sort(reverse=False)
    
    for i in range(n - 1):
        if a[i] < a[i + 1]:
            if u <= float((i + 1) * (a[i + 1] - a[i])):
                for j in range (i + 1):
                    a[j] += float(u / (i + 1))
                u = 0.0
                break
            else:
                for j in range (i):
                    a[j] = a[i + 1]
                u -= ((i + 1) * (a[i + 1] - a[i]))
                a[i] = a[i + 1]
    for i in range(n):
        a[i] += float(u / n)
        x *= a[i]
    print("{:.6f}".format(x))