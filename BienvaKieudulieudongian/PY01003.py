def run():
    n = input()[::-1]
    count = {} 
    for i in range(0, len(n)):
        count[i] = int(n[i])
    for i in range(0, len(n) - 1):
        if count[i] >= 5:
            count[i] = 0
            count[i + 1] += 1
        else:
            count[i] = 0
    res = ""
    for i in count:
        res = str(count[i]) + res
    print(res)

def main():
    t = int(input())
    for i in range(0, t):
        run()    

main()
