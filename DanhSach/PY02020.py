def run():
    n = int(input())
    a = [float(i) for i in input().split()]
    a.sort()
    Sum = 0
    dem = 0
    for i in range(1, n):
        if a[i] != a[0] and a[i] != a[n - 1]:
            dem += 1
            Sum += a[i]
    print("{:.2f}".format(float(Sum / dem)))       

run()