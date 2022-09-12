t = int(input())
while t > 0:
    t -= 1
    n, m, l = map(int, input().split())
    a = [[0]] * 505

    for i in range(n):
        a[i] = [int(x) for x in input().split()]

    p = n - l + 1
    q = m - l + 1
    for i in range(0, n):
        for j in range(0, m):
            if i == 0 or j == 0:
                if j == 0:
                    a[i][j] += a[i - 1][j]
                if i == 0:
                    a[i][j] += a[i][j - 1]
            else:
                a[i][j] += a[i][j - 1] + a[i - 1][j] - a[i - 1][j - 1]

    # for i in range(n):
    #     for j in range(m):
    #         print(a[i][j], end = ' ')
    #     print()

    for i in range (0, p):
        for j in range(0, q):
            if i == 0 and j == 0:
                print(int(a[i + l - 1][j + l - 1] / (l * l)), end = ' ')
            elif i == 0:
                print(int((a[i + l - 1][j + l - 1] - a[i + l - 1][j - 1]) / (l * l)), end = ' ')
            elif j == 0:
                print(int((a[i + l - 1][j + l - 1] - a[i - 1][j + l - 1]) / (l * l)), end = ' ')
            else:
                print(int((a[i + l - 1][j + l - 1] - a[i - 1][j + l - 1] - a[i + l - 1][j - 1] + a[i - 1][j - 1]) / (l * l)), end = ' ')
        print()
        
# import math
# t = int(input())
# while t > 0:
#     a, s, kq = [], [], []
#     n, m, p = map(int, input().split())
#     for i in range(0, n):
#         b, b1, b2 = [], [], []
#         pos = 0
#         j = 0
#         for x in input().split():
#             b1.append(int(x))
#             j += 1
#             if (j < p):
#                 pos += int(x)
#             elif j == p:
#                 pos += int(x)
#                 b.append(pos)
#             else:
#                 pos = pos+int(x) - b1[j - p - 1]
#                 b.append(pos)
#         a.append(b)
#     # print(a)
#     for i in range(0, n-p+1):
#         for j in range(0, m-p+1):
#             print(int(a[i][j]/(p*p)), end=' ')
#         print()
#     t -= 1
