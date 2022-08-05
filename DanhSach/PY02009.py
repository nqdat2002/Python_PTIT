def solve():
    f = [0] * 1001
    n = int(input())
    for i in range(n):
        f[int(input())] += 1
    dem = -1
    ans = -1
    for i in range(1001):
        if f[i] > dem:
            dem = f[i]
            ans = i
    print(ans)
    
T  = int(input())
for t in range(T):
    solve()