def solve():
    s = input().split('.')
    if len(s) != 4:
        print('NO')
        return
    for i in s:
        if i.isdigit():
            if int(i) > 255 or int(i) < 0:
                print('NO')
                return
        else:
            print('NO')
            return
        
    print('YES')

T = int(input())

while T > 0:
    solve()
    T -= 1