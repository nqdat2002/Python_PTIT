def Mul(n):
    a = 1
    n = str(n)
    for i in range(0, len(n)):
        a = a * int(n[i])
    return a

def take_second(tmp):
    return (tmp[1], tmp[0])

def run():
    n = int(input())
    lst = [int(i) for i in input().split()]
    res = []
    for i in range(n):
        tmp = (lst[i], Mul(int(lst[i])))
        res.append(tmp)
    res = sorted(res, key=take_second)
    kq = ""
    for i in range(n):
        kq += str(res[i][0]) + " "
    print(kq)
    
def main():
    t = int(input())
    for i in range(t):
        run()

main()
