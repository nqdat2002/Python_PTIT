t = int(input())
while t > 0:
    t -= 1
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    ok = True
    for i in b: 
        if i < 0: 
            if i == max(b) and ok:
                ok = False
                print(a[1], end=" ")
            print(i, end=" ")
    for i in b:
        if i >= 0:
            if i == max(b) and ok:
                ok = False
                print(a[1], end=" ")
            print(i, end=" ")
    print()   