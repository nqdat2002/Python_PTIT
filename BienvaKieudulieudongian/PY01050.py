def kiemTraXau(s):
    if s.count('A') > s.count('B') or s.count('B') > s.count('C') or s.count('A') == 0 or s.count('B') == 0 or s.count('C') == 0:
        return 0
    return 1

def inXau(a, n):
    k = len(a)
    Try(a, '', k, n)
    
def Try(a, prefix, k, n):
    if n == 0:
        if kiemTraXau(prefix):
            print(prefix)
        return
    for i in range(k):
        newprefix = prefix + a[i]
        Try(a, newprefix, k, n - 1)

n = int(input())
t = 3
while t <= n:
    a = ['A', 'B', 'C']
    inXau(a, t)
    t += 1