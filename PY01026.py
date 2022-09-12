def solve(t):
    s = input()
    s1 = input()
    print("Test " + str(Test) + ":", end=' ')
    if(len(s) != len(s1)):
        print("NO")
        return
    s = sorted(s)
    s1 = sorted(s1)
    for i in range(len(s)):
        if s[i] != s1[i]:
            print("NO")
            return
    print("YES")
    
T = int(input())
for Test in range(1, T + 1):
    solve(Test)
