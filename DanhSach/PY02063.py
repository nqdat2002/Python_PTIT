
n = int(input())
l = list(int(x) for x in input().split())
l.sort()

x1 = l[0] * l[1]
x2 = l[0] * l[1] * l[-1]
x3 = l[-1]* l[-2]
x4 = l[-1] * l[-2] * l[-3]

print(max([x1,x2,x3,x4]))