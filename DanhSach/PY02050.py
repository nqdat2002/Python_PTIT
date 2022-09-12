test = int(input())
for t in range(test):
    n = int(input())
    a = [int(i)for i in input().split()]
    r = [-1]*100005
    stack = []
    for i in range(n-1,-1,-1):
        if len(stack) ==0 or a[stack[-1]] >= a[i]:
            stack.append(i)
        else:
            while len(stack) != 0 and a[i] > a[stack[-1]]:
                r[stack[-1]] = i
                stack.pop()
            stack.append(i)
    for i in range(n):
        print(i - r[i],end=" ")
    print("")