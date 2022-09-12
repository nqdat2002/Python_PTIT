def solve():
    s = input()
    sum = 0
    for i in s:
        sum += int(i)
    s = str(sum)
    if len(s) < 2:
        print("NO")
        return
    if s == s[::-1]:
        print("YES")
        return
    print("NO")

T = int(input())

while T != 0:
    solve()
    T -= 1