def solve(n):
    L = []
    for i in range(n):
        L.append(int(input()))
    L = sorted(L)
    if L[0] == L[len(L) - 1]:
        print("BANG NHAU")
    else:
        print(L[0], L[len(L) - 1])

while True:
    n = int(input())
    if n == 0:
        break
    solve(n)