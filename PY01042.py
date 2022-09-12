def solve(n):
    for i in n:
        if i != '0' and i != '1' and i != '2':
            print("NO")
            return
    print("YES")

t = int(input())
while t > 0:
    t -= 1
    n = input()
    solve(n)