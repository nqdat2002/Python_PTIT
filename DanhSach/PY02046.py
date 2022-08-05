
def check(a):
    if a < 2:
        return 0
    for i in range(2, a + 1):
        if i * i > a:
            break
        if a % i == 0:
            return 0
    return 1

def solve():
    f = [0] * 1001
    n = int(input())
    L = []
    total_list = []
    for i in input().split():
        L.append(int(i))
        f[L[-1]] += 1
    for i in L:
        if f[i] > 0:
            total_list.append(i)
            f[i] = 0
    del f, L

    n = len(total_list)
    sum = [0]
    for i in total_list:
        sum.append(sum[-1] + i)

    for i in range(1, n + 1):
        if check(sum[i]) * check(sum[-1] - sum[i]):
            print(i - 1)
            return
    print("NOT FOUND")
    



solve()