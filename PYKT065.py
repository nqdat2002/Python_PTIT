prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
a = []
n = len(prime)
b = [0] * n

def Try(i):
    for j in range (0, 2):
        b[i] = j
        if i == n - 1:
            pos = 1
            for k in range (n):
                if b[k] == 1:
                    pos = pos * prime[k]
            a.append(pos)
            pos = 1
        else:
            Try(i + 1)

Try(0)
a.sort(reverse = True)
while True:
    s = input()
    if s == '-1':
        break
    x, y = s.split()
    x = int(x)
    y = int(y)
    k = int(input())
    res = 0
    # for i in range (len(a) - 1, -1, -1):    
        

