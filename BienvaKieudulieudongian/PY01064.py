def Try(n, k) :
    if(k == pow(2, n - 1)):
        return n
    if(k < pow(2, n - 1)):
        return Try(n - 1, k)
    return Try(n - 1, k - pow(2, n - 1))


t = int(input())
while t > 0: 
    n, k = map(int, input().split())
    print(chr(Try(n, k) + 64))
    t = t - 1