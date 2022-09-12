for i in range(int(input())):
    s = input()
    stack_ngoac = []
    stack_so = []
    count = 1
    a = []
    for i in s:
        if i == '(':
            stack_ngoac.append(i)
            stack_so.append(count)
            a.append(stack_so[len(stack_so)-1])
            count += 1
        elif i == ')':
            if len(stack_ngoac)>0:
                stack_ngoac.pop()
                a.append(stack_so[len(stack_so)-1])
                stack_so.pop()
    for i in a: print(i, end=' ')
    print()