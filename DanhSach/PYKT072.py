def roated(s):
    r = s[1:len(s)]
    return r + s[0]

n = int(input())
t = n
minres = 1000 * 1000 * 1000
check = 1
a = []
while t > 0:
    t -= 1
    s = input()
    a.append(s)
    
for i in range(0, len(a[0])):
    sum = i
    for j in range(1, n):
        cnt = 0
        if a[0] != a[j]:
            x = a[j]
            while a[0] != x:
                cnt += 1
                x = roated(x)
                if cnt > len(a[0]) - 1:
                    check = 0
                    break
        if check == 0:
            break
        sum += cnt
    if check == 0:
        break
    if sum < minres:
        minres = sum
    a[0] = roated(a[0])
if check != 0:
    print(minres)
else:
    print(-1)
    