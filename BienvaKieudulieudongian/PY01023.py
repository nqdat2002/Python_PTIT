import math

def run():
    n = int(input())
    res = "1"
    for i in range(2, int(math.sqrt(n)) + 1):
        dem = 0
        while n % i == 0:
            n = n / i
            dem += 1
        if dem > 0:
            res = res + " * " + str(i) + "^" + str(dem)
    if n > 1:
        res = res + " * " + str(int(n)) + "^1" 
    print(res)

def main():
    t = int(input())
    for i in range(0, t):
        run()    

main()
