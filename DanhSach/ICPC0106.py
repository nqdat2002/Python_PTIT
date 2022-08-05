def cs(s):
    so = 0
    for i in range(0, len(s)):
        if s[i] == "1":
            so += pow(2, len(s) - i - 1)
    return so    

def solve(n, b):
    sb = ""
    while (n > 0):
        m = n % b
        if m >= 10:
            sb += str(chr(55 + m))
        else:
            sb += str(m)
        n = n // b
    print(sb[::-1])

t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    s = input()
    solve(cs(s), n)