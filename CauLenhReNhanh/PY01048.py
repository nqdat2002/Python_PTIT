def isSumOfPositiveInterger(a, b):
    if a + b - 1 > 0 and (a + b - 1 ) % 2 == 0:
        cuoi = (a + b - 1 ) / 2
        dau = a - cuoi
        if cuoi > dau and dau > 0:
            return True
    return False

def solve():
    n = int (input())
    n *= 2
    dem = 0
    for i in range(2, n):
        if n % i == 0 and isSumOfPositiveInterger(int (n / i), i) == True:
            dem += 1
        if i * i > n:
            break
    print(dem)


T = int(input())
for i in range (T):
    solve()