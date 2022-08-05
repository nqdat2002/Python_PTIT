def solve(a, b, c, d):
    dem = 0
    while not(a == b and b == c and c == d):
        dem += 1
        a1 = abs(a - b)
        a2 = abs(b - c)
        a3 = abs(c - d)
        a4 = abs(d - a)
        a = a1
        b = a2
        c = a3
        d = a4
    print(dem)

while True:
    a, b, c, d = map(int, input().split())
    if a == 0 and b == 0 and c == 0 and d == 0:
        break
    solve(a, b, c, d)