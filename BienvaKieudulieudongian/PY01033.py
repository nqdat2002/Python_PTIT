def check(a, b):
    while a * b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    if a + b == 1:
        return 1
    else: 
        return 0

L, R = map(int, input().split())

lst = []
B = []
for i in range(L, R):
    a = []
    for j in range(i + 1, R + 1):
        if check(i, j) == 1:
            a.append(j)
    if len(a) > 0:
        lst.append(a)
        B.append(i)
for i in range (len(B)):
    for j in range (len(lst[i])):
        for k in range(j + 1, len(lst[i])):
            if check(lst[i][j], lst[i][k]) == 1:
                print('(' + str(B[i]) + ', ' + str(lst[i][j]) + ', ' + str(lst[i][k]) + ')')
            
        