def solve():
    s = input()
    sum = 0
    mul = 1
    ok = 1
    for i in range(len(s)):
        if i % 2 == 1:
            sum += int(s[i])
        else:
            if s[i] == '0':
                continue
            else:
                ok = 0
                mul *= int(s[i])
    if ok == 1:
        mul = 0
    print(mul, sum)


T = int(input())
while T != 0:
    solve()
    T -= 1