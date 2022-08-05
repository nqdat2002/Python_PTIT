def solve():
    s = input()
    s = sorted(s)
    sum = 0
    vt = -1
    for i in range(len(s)):
        if s[i] >= '0' and s[i] <= '9':
            sum += int(s[i])
        else:
            vt = i
            break
    if vt == -1:
        vt = len(s)
    for i in range(vt, len(s)):
        print(s[i], end = '')
    print(sum)

T = int(input())
while T != 0:
    solve()
    T -= 1