def run():
    s = input()
    dem = 1
    kq = ""
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            dem += 1
        else:
            kq = kq + str(dem) + s[i-1]
            dem = 1
    kq = kq + str(dem) + s[len(s) - 1]    
    print(kq)

def main():
    t = int(input())
    for i in range(t):
        run()

main()