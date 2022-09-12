def gcd(a, b):
    while a > 0:
        if a < b:
            a, b = b, a
        a = a % b
    return b

def run():
    n = input()
    if gcd(int(n), int(n[::-1])) == 1:
        print("YES")
    else:
        print("NO")

def main():
    t = int(input())
    for i in range(0, t):
        run()    

main()
