from typing import no_type_check


n = int (input())
L = []
for i in range(n):
    sum = 0
    for j in input().split():
        sum += int(j)
    L.append(sum)
if n == 1:
    print (L[0])
elif n == 2:
    print (int (sum / 2),int (sum / 2))
else:
    sum = 0
    for i in L:
        sum += i
    sum = int (sum / (int(n - 1) * 2))

    for i in L:
        print(int ((i - sum) / (n - 2)), end = ' ')