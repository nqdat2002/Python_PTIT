def solve():
    s = input()
    sum = 0
    for i in range(len(s)):
        a = int(s[i])
        if i % 2 != a % 2:
            print("NO")
            return
        sum += a
    for i in range(2, sum + 1):
        if i * i > sum:
            break
        if sum % i == 0:
            print("NO")
            return        
    print("YES")

T = int(input())

while T != 0:
    solve()
    T -= 1