def solve():
    s = input()
    if len(s) > 4:
        s = s[-4 : ]
    tmp = int(s)
    if tmp < 2:
        print("NO")
        return
    for i in range(2, tmp + 1):
        if tmp % i == 0:
            print("NO")
            return
        if i * i > tmp:
            break
    print("YES")

T = int(input())
while T != 0:
    solve()
    T -= 1