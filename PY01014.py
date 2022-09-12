def main():
    a = [int(i) for i in input().split()]
    x = int(a[2]) - int(a[0])
    if int(a[2]) <= int(a[0]):
        print(-1)
        return
    n = int(a[1]) - int(a[0]) % int(a[1])
    if n > x:
        print(-1)
        return
    res = ""
    while n <= x:
        res += str(n) + " "
        n += int(a[1])
    print(res)

main()