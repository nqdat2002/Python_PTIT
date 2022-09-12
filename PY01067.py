def Run():
    A = int(input())
    n = 3
    a = 0
    while A > 0:
        S = ''
        i = a + 1
        a = i
        while i > 0:
            C = i % n
            S = S+str(i % n)
            i = int(i/n)
        if LON50(S[::-1]):
            A -= 1
            print(S[::-1], end=' ')
    print()


def LON50(A):
    count = 0
    for i in A:
        if i == '2':
            count += 1
    if count > len(A)/2:
        return True
    else:
        return False


B = int(input())
while (B > 0):
    B -= 1
    Run()
