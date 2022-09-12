def nguyenTo(a):
    if a < 2:
        return 0
    for i in range(2, a + 1):
        if i * i > a:
            break
        if a % i == 0:
            return 0
    return 1

def solve():
    s = input()
    dau = s[0:3]
    cuoi = s[-3:]
    if nguyenTo(int(dau)) * nguyenTo(int(cuoi)) == 1:
        print("YES")
    else:
        print("NO")


T = int(input())
while T != 0:
  solve()
  T -= 1