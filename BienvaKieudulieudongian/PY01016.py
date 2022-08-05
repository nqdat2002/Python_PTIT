def so(a):
    if(a < '1'):
        return False
    if(a > '9'):
        return False
    return True

def run():
    a = input()
    b = ""
    for i in range(len(a)):
        if(so(a[i])):
            for j in range(int(a[i])): 
                b = b + a[i-1]
    print(b)

def main():
    t = int(input())
    for i in range(t):
        run()

main()
