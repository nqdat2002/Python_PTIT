def check(i):
    if abs(ord(s1[i]) - ord(s1[i - 1])) == abs(ord(s2[i]) - ord(s2[i - 1])):
        return True
    else:
        return False

testCase = int(input())
while testCase > 0:
    s1 = str(input())
    tmp = list(reversed(s1))
    s2 = ''.join(tmp)
    no = 0
    for i in range(len(s1)):
        if check(i) == False:
            no = 1
            break
    if no == 1:
        print("NO")
    else:
        print("YES")
    testCase -= 1