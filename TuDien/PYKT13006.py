f = [0] * 1000001
f[0] = 2
f[1] = 6
for i in range (2, 100001):
    f[i] = 6 * f[i - 1] - 4 * f[i - 2]
    
t = int(input())
for i in range(t):
    n = int(input())
    s = str(f[n] - 1)
    if len(s) == 1:
        print('Case #' + str(i + 1) + ': ' + '0' + '0' + s)
    elif len(s) == 2:
        print('Case #' + str(i + 1) + ': ' + '0' + s)
    else:
        print('Case #' + str(i + 1) + ': ' + s[len(s) - 3: len(s)])