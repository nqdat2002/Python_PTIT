import re
def solve():
    s = input()
    tmp = input()
    ans = re.findall(tmp, s)
    print(len(ans))
    
T = int(input())
while T:
    solve()
    T -= 1