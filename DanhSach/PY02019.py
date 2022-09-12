import math

n = int(input())
x = [int(x) for x in input().split()]
x.sort()
for i in range(n - 1):
    for j in range(i + 1, n):
        if math.gcd(x[i], x[j]) == 1:
            print(x[i], x[j])
