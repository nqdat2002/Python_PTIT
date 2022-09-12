def run():
    a = input()
    n = len(a)
    if (a[n-2] == '8'):
        if (a[n-1] == '6'):
            print("YES")
        elif (a[n-1] != '6'):
            print("NO")
    elif (a[n-2] != '8'):
        print("NO")

def main():
    t = int(input())
    for i in range(t):
        run()

main()
