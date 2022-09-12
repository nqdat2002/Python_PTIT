import itertools

s = input()
res = itertools.permutations(s)
for i in res:
    print(*i, sep="")