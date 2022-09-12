def solve():
    s = input()
    if len(s) % 2 == 0 or len(s) < 2 or s[0] == s[1]:
        print("NO")
        return
    i = 2
    while i < len(s):
        if s[i] != s[i - 2]:
            print("NO")
            return
        i += 2
    print("YES")

T = int(input())

while T != 0:
    solve()
    T -= 1