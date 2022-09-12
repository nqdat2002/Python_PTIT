def solve():
    dic = {}
    n, m = map(int, input().split())
    for i in input().split():
        a = int(i)
        try:
            dic[a] += 1
        except:
            dic[a] = 1
    dic = sorted(dic.items(), key = lambda x : (x[1], -x[0]))
    # print(dic)
    if dic[0][1] == dic[-1][1]:
        print("NONE")
        return
    tmp = len(dic) - 1
    m = tmp
    while dic[tmp][1] == dic[m][1]:
        tmp -= 1
    print(dic[tmp][0])
solve()