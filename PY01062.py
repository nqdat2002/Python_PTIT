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
    if nguyenTo(len(s)) == 0:
        print("NO")
        return
    dem = 0
    for i in s:
        dem += nguyenTo(int(i))
    if dem > len(s) - dem:
        print("YES")
    else:
        print("NO")


T = int(input())
while T != 0:
  solve()
  T -= 1