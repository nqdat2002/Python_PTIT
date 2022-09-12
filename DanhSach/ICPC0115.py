n = int(input())
L = [1]
ans = 1
for i in range(1, 10):
    ans *= i
    L.append(ans)

for i in range(n):
    num = input()
    sum = 0
    for j in num:
        sum += L[int(j)]
    if sum == int(num):
        print('Yes')
    else:
        print('No')
