def reversed(n):
    return int(str(n)[::-1])

def solve(n):
    sum = n
    while sum % 7 != 0:
        sum += reversed(sum)
    return sum

t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    print(solve(n))
