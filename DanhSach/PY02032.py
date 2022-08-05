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
        A[a] = 1
    i += 2

B.sort()
for i in B:
    print(i, end = ' ')

