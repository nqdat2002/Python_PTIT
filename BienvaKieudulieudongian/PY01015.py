def run():
    a = input()
    ok = True
    for i in range(1, len(a)):
        if (a[i] < a[i-1]):
            print("NO")
            ok = False
            break
    if ok == True:
        print("YES")

def main():
    t = int(input())
    for i in range(t):
        run()
    
main()
