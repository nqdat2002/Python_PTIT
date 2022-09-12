
def Try(a, b, c, n):
    if(n == 1):
        print(a + " -> " + c)
    else:
        Try(a, c, b, n - 1)
        print(a + " -> " + c)
        Try(b, a, c, n - 1)

n = int(input())
Try('A', 'B', 'C', n)