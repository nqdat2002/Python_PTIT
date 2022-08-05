def run():
    s = input()
    ok = True
    for i in s:
        if i != '4' and i != '7':
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