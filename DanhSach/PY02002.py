f = {}
def pre():
    f[1] = 1
    f[2] = 1
    for i in range(3, 93):
        f[i] = f[i - 1] + f[i - 2]

def run():
    a = input()
    a = a.split()
    res = ""
    for i in range(int(a[0]), int(a[1]) + 1):
        res += str(f[i]) + " "
    print(res)

def main():
    pre()
    t = int(input())
    for i in range(0, t):
        run()    

main()
