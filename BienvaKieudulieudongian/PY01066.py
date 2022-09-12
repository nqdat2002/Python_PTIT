def solve():
    s = input()
    new_s = s[:: -1]

    for i in range(len(s) - 1):
        if abs(ord(s[i]) - ord(s[i + 1])) != abs(ord(new_s[i]) - ord(new_s[i + 1])):
            print("NO")
            return
    print("YES")

T = int(input())
while T != 0:
    solve()
    T -= 1

