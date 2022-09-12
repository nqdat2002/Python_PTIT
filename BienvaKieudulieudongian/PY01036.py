def solve():
    n = int (input())
    sum = 0.0
    if n % 2 == 1:
        for i in range (1, n + 1, 2):
            sum += 1/i
    if n % 2 == 0:
        for i in range (2, n + 1, 2):
            sum += 1/i
    sum = str(round(sum, 6))
    dem = 0
    dd = 0
    for i in sum:
        if dd == 1:
            dem += 1
        if  i == '.':
            dd = 1
    while dem < 6:
        sum = sum + '0'
        dem += 1
    print(sum)
T = int(input())
while T:
    solve()
    T -= 1