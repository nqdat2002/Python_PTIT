f = [0] * 501

def nguyen_to(a):
    if a < 2: 
        return 0

    for i in range(2, a):
        if i * i > a:
            break
        if a % i == 0:
            return 0
    return 1
def arrayNguyenTo():
    for i in range(2, 501):
        f[i] = nguyen_to(i)

def solve():
    s = input()
    for i in range(len(s)):
        if f[i] != nguyen_to(int(s[i])):
            print("NO")
            return
    print("YES")

arrayNguyenTo()
T = int(input())
while T != 0:
    solve()
    T -= 1