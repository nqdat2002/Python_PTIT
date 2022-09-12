import itertools


def Run():
    A = [int(i) for i in input().split()]
    B = input().split()
    B1 = []
    for i in range(A[0]):
        if B[i] not in B1:
            B1.append(B[i])
    for i in list(itertools.combinations(sorted(B1), A[1])):
        S = ''
        for j in i:
            S = f'{S} {j}'
        print(S.strip())


Run()
