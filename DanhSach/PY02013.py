def check(Y, a):
    for i in Y:
        if i == a:
            return True
    return False

def solve(n):
    Y = [n]
    while n != 1:
        if n % 2 == 0:
            n = int (n / 2)
        else:
            n = n * 3 + 1
        if check(Y, n) == 0:
            Y.append(n)
    print(len(Y))

while True:
    n = int(input())
    if n == 0:
        break
    solve(n)