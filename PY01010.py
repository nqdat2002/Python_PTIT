def run():
    s = input()
    n = len(s)
    if n >= 4 and s[0] == s[n - 2] and s[1] == s[n - 1]:
        print("YES")
    else:
        print("NO")

def main():
    t = int(input())
    for i in range(t):
        run()

main()
    