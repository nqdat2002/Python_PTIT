f = [0] * 30001
n = int(input())
for i in input().split():
    f[int(i)] = 1
for i in range(1, 30001):
    if f[i] == 0:
        print(i)
        break