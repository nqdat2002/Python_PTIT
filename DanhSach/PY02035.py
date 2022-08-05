s = input()

n = len(s)
if len(s) % 2 == 1:
    n -= 1
A = [0] * 100
B = []
i = 0
while i < n:
    a = int(s[i:i+2])
    if A[a] == 0:
        B.append(a)
    A[a] += 1
    i += 2

k = int(input())
L = []
for i in B:
    if A[i] >= k:
        L.append([i, A[i]])
        A[i] = 0
L = sorted(L, key = lambda x : x[0])
if len(L) == 0:
    print("NOT FOUND")
else:
    for i in L:
        print(i[0], i[1])


