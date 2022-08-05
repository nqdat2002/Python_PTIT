def solve():
    s = input()
    sum = 0
    for i in s:
        sum += int(i)
    for i in range(2, sum + 1):
        if sum % i == 0:
            print("NO")
            return
        if i * i > sum:
            break
    print("YES")

T = int(input())

while T != 0:
    solve()
    T -= 1