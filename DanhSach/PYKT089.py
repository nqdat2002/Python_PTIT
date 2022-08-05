n = int(input())
C = []
L = []
ans = []
while n != len(L) + len (C):
    for i in input().split():
        ans.append(int(i))
        if int (i) % 2 == 1:
            L.append(int (i))
        else:
            C.append(int(i))
C.sort()
L.sort(reverse = True)
indc = 0
indl = 0
for i in ans:
    if i % 2 == 0:
        print(C[indc], end = ' ')
        indc += 1
    else:
        print(L[indl], end = ' ')
        indl += 1