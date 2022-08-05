import re
t = int(input())

while t > 0:
    t -= 1
    s = input()
    tmp = re.findall('[\d]+',s)
    l = [int(i) for i in tmp]
    print(min(l))