
def countNumber(n):
    count = 0
    for i in range(0, 10):
        if str(i) in n:
            count += 1
    if count >= 3:
        return 1
    return 0

def increase(n, v):
    for i in range(1, v + 1):
        if n[i] <= n[i - 1]:
            return 0
    return 1        

def decrease(n, v):
    for i in range(v, len(n) - 1):
        if n[i] <= n[i + 1]:
            return 0
    return 1        

def solve(n):
    if countNumber(n) == 0:
        print("NO")
        return
    for  i in range(1, len(n) - 1):
        if increase(n, i) and decrease(n, i):
            print("YES")
            return
    print("NO")
        

t = int(input())
while t > 0:
    t -= 1
    n = input()
    solve(n)