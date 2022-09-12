def solve(n):
    for i in range(2, len(n)):
        if n[i] != n[i - 2]:
            print("NO")
            return
    for i in range(3, len(n)):
        if n[i] != n[i - 2]:
            print("NO")
            return
    print("YES")

t = int(input())
while t > 0:
    t -= 1
    n = input()
    solve(n)