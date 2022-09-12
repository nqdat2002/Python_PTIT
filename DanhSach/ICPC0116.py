n = int(input())

for i in range(n):
    s = input()
    if s[0] == s[-1]:
        print('YES')
    else:
        print('NO')