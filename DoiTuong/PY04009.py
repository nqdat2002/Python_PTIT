def solve():
    a,b,c,d = map(int, input().split())
    A = complex(a, b)
    B = complex(c, d)
    C = (A + B) * A
    D = (A + B)**2
    
    a = int(C.real)
    b = int(C.imag)
    ans = ''
    if b < 0:
        ans = str(a) + ' - ' + str(abs(b)) + 'i'
    else:
        ans = str(a) + ' + ' + str(b) + 'i'
    ans = ans + ', '
    print(ans, end = '')

    a = int(D.real)
    b = int(D.imag)
    if b < 0:
        ans = str(a) + ' - ' + str(abs(b)) + 'i'
    else:
        ans = str(a) + ' + ' + str(b) + 'i'
    print(ans)

T = int(input())
while T > 0:
    solve()
    T -= 1