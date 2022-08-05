
from itertools import permutations
import math
# WA
T = int(input())
for t in range(T):
    n = int(input())
    s = ""
    for i in range(1, n + 1): s = str(i) + s
    res = permutations(s)
    print(math.factorial(n))
    for i in res:
        print(**i, step = '', end = ' ')
    