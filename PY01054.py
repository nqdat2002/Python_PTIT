def solve():
    s = input()
    mul = 1
    for i in s:
        if i != '0':
            mul *= int(i)
    print(mul)

T = int(input())

while T != 0:
    solve()
    T -= 1