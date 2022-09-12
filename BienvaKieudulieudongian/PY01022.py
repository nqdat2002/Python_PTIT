def solve():
    s = input()
    res = 0
    while True:
        res += 1
        sum = 0
        for i in s:
            if i == '-':
                sum += (ord('-') - ord('0'))
            else:
                sum += int(i)
        if sum < 10:
            print (res)
            return
        s = str(sum)
solve()
