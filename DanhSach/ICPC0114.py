def nguyento(num):
    for i in range(2, num):
        if i * i > num:
            break
        if num % i == 0:
            return False
    
    return True

def solve():
    s = '2357'
    num = input()
    for i in num:
        if i not in s:
            print('No')
            return
    if nguyento(int(num)) and nguyento(int(num[::-1])):
        print('Yes')
    else:
        print('No')

n = int(input())

for i in range(n):
    solve()