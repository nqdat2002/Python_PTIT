class calc:
    def __init__(self,a,b) -> None:
        self.a=a
        self.b=b

n, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
Data = []
for i in range(n):
    Data.append(calc(a[i],b[i]))
Data.sort(reverse = True, key=lambda x : x.b - x.a)
sum = 0
for i in range(k):
    sum += Data[i].a
for i in range(k, n):
    if(Data[i].b > Data[i].a):
        sum += Data[i].a
    else:
        sum += Data[i].b
print(sum)