def ChiaHetCho10(s):
    tong = 0
    for i in s:
        tong = tong + int(i)
    if tong % 10 == 0:
        return True
    else:
        return False 

def CachDeu(s):
    for i in range(1, len(s)):
        so = int(s[i]) - int(s[i-1])
        if so != -2 and so != 2:
            return False
    return True 

def run():
    s = input()
    if CachDeu(s) and ChiaHetCho10(s):
        print("YES")
    else:
        print("NO")

def main():
    t = int(input())
    for i in range(t):
        run()

main()