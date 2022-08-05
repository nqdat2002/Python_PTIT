def solve():
    n = int(input())
    a = [int (i) for i in input().split()]
    b = [int (i) for i in input().split()]
    a = sorted(a)
    b = sorted(b)
    for i in range(n):
        if a[i] > b[i]:
            print("NO")
            return
    print("YES")


T = int(input())

while T:
    solve()
    T -= 1