def Eratosthens():
    f = [1] * 10001
    f[0] = 0
    f[1] = 0
    for i in range (2, 10001):
        if f[i] == 0:
            continue
        for j in range(i * i, 10001, i):
            f[j] = 0
    return f


f = Eratosthens()

t = int(input())

while t > 0:
    t -= 1
    num = input()
    if f[len(num)] == 0:
        print('NO')
    else:
        dem = 0
        for i in num:
            if f[int(i)] == 1:
                dem += 1
        
        if dem > len(num) - dem:
            print ('YES')
        else:
            print('NO')