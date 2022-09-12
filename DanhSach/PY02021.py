def BS_L(l, r, value, a):
    res = -1
    while l <= r:
        mid = int((l + r) / 2)
        if a[mid] <= value:
            res = mid
            l = mid + 1
        else:
            r = mid - 1
    return res

def BS_U(l, r, value, a):
    res = -1
    while l <= r:
        mid = int((l + r) / 2)
        if a[mid] >= value:
            res = mid
            l = mid + 1
        else:
            r = mid - 1
    return res

def solve():
    n, m, k = map (int, input().split())
    A = [int (i) for i in input().split()]
    B = [int (i) for i in input().split()]
    C = [int (i) for i in input().split()]

    i = 0
    j = 0
    h = 0
    dd = 1
    while i < n and j < m and h < k:
        if A[i] == B[j] and B[j] == C[h]:
            print(A[i], end = ' ')
            i += 1
            j += 1
            h += 1
            dd = 0
            continue
        if A[i] < B[j] or A[i] < C[h]:
            i += 1
            continue
        if B[j] < A[i] or B[j] < C[h]:
            j+= 1
            continue
        if C[h] < A[i] or C[h] < B[j]:
            h += 1
    if dd == 1:
        print("NO")
        return
    print()

T = int(input())
for i in range(T):
    solve()

    