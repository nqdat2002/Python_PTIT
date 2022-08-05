def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else: b %= a
    return a + b

n = int(input())
a = [int(i) for i in input().split()]
a = sorted(a)
for i in range(0, len(a)):
    for j in range(i + 1, len(a)):
        if gcd(a[i], a[j]) == 1:
            print(a[i], a[j])