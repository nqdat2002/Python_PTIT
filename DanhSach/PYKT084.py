n = int(input())
L = []
i = 0
while i < n:
    s = input()
    i += 1
    if s == '':
        while s == '' and i < n:
            s = input()
            i += 1
        L.append([s, -1])
    if len(L) == 0:
        L.append([s, -1])
    L[-1][1] += 1
    


for i in L:
    print(i[0] + ':', i[1])
