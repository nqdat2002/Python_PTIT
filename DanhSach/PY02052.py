n = int(input())

sum_up = 0
sum_down = 0
for i in range(n):
    L = [int(j) for j in input().split()]
    for j in range(n):
        if j == i:
            continue
        if j < i:
            sum_up += int(L[j])
        else:
            sum_down += int(L[j])
k = int(input())

if abs(sum_down - sum_up) > k:
    print("NO")
else:
    print("YES")
print(abs(sum_down - sum_up))