s = input()

n = len(s)
if len(s) % 2 == 1:
    n -= 1
A = [0] * 100
B = []
i = 0
while i < n:
    a = int(s[i:i+2])
    A[a] += 1
    B.append(a)
    i += 2
for i in B:
    if A[i] > 0:
        print(i, A[i])
        A[i] = 0

