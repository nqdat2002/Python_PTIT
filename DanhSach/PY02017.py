def BS(mylist, value, l, r):
    res = -1
    while l <= r:
        mid = int ((l + r) / 2)
        if mylist[mid] <= value:
            res = mid
            l = mid + 1
        else:
            r = mid - 1
    return res

def solve():
    n = int (input())
    mylist = [int(i) for i in input().split()]
    mylist.sort()
    i = 0
    while i < n:
        ind = BS(mylist, mylist[i], i, n - 1)
        if (ind - i + 1) % 2 == 1:
            print(mylist[i])
            return
        i = ind + 1

T = int(input())
while T != 0:
    solve()
    T -= 1