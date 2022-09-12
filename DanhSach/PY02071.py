a = [0] * 100
b = []
def Try(i, k, s, n):
    for j in range(k, 0, -1):
        if s + j <= n:
            a[i] = j
            s += j
            if s == n:
                strs = '('
                for x in range(1, i):
                    strs += str(a[x]) + ' '
                strs += str(a[i]) + ')'
                b.append(strs)
            else:
                Try(i + 1, j, s, n)
            s -= j
t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    a = [0] * 100
    b.clear()
    Try(1, n, 0, n)
    print(len(b))
    for x in b:
        print(x, end = ' ')
    print()
    