def solve():
    s = input()
    sum = 0
    for i in s:
        sum += int(i)
    if sum % 3 == 0:
        print("YES")
        return
    print("NO")

T = int(input())

while T != 0:
    solve()
    T -= 1