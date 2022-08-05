
T = int (input())
while T != 0:
    s = input().split()
    a = int(s[0])
    k = int(s[1])
    res = ""
    while a != 0:
        b = a % k
        if(b <= 9):
            res = str(b) + res
        else:
            c = b - 10 + ord('A')
            res = chr(c) + res
        a = int (a / k)
    print(res)
    T -= 1