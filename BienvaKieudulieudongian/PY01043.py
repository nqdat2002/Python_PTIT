def thuan_nghich(n):
    s1 = n[::-1]
    if s1 == n:
        return True
    return False

def chan(n):
    for i in n:
        if int(i) % 2 != 0:
            return False
    return True

def run():
    n = int(input())
    i = 22
    tmp = 100
    while i < n:
        if thuan_nghich(str(i)) and chan(str(i)):
            print(i, end=" ")
        if i == tmp:
            i = tmp * 10
            tmp *= 100
        else: i += 2
    print()

def main():
    t = int(input())
    for i in range(0, t):
        run()    

main()
