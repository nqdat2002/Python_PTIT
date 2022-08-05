def solve():
    n = int (input())
    L = []
    L = [int(i) for i in input().split()]
    ans  = -1
    res = -1
    for i in L:
        tmp = 0
        for j in L:
            if j > i: tmp = tmp + j - i
            else: tmp = tmp + i - j
        if tmp < ans or ans == -1:
            ans = tmp
            res = i
    print(ans, res)

solve()