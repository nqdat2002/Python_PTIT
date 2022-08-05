def run():
    n = int(input())
    tren = 0
    duoi = 0
    for i in range(n):
        x = [int(i) for i in input().split()]
        for j in range(0, n - i - 1):
            tren += x[j]
        for j in range(n - i, n):
            duoi += x[j]
    tmp = abs(tren - duoi)
    k = int(input())
    if(tmp <= k):
        print("YES")
    else:
        print("NO")
    print(tmp)


run()