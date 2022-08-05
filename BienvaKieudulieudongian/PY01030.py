def nguyen_to_cung_nhau(a, b):
    while a * b != 0:
        if a >= b:
            a %= b
        else:
            b %= a
    return a + b

n, k = map(int, input().split())
b = 10 ** k
a = b // 10

dem = 0
for i in range(a, b):
    if nguyen_to_cung_nhau(i, n) == 1:
        dem += 1
        print(i, end = ' ')
        if dem % 10 == 0:
            print()

