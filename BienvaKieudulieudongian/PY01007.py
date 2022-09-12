import math

def run():
    n = input()
    n = n.split()
    x = float(n[2]) / float(n[0])
    tmp = 0.0
    cs = 1 + float(n[1]) / 100
    i = 0
    while tmp < x:
        i += 1
        tmp = math.pow(cs, i)
    print(i)

def main():
    t = int(input())
    for i in range(0, t):
        run()    

main()