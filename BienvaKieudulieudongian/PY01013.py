import math

def gcd(a, b):
    while a > 0:
        if a < b:
            a, b = b, a
        a = a % b
    return b

def isPrime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

def sumOfDigits(n):
    sum = 0
    for i in str(n):
        sum += int(i)
    return sum

def run():
    x, y = input().split()
    x = int(x)
    y = int(y)
    if isPrime(sumOfDigits(gcd(x, y))):
        print("YES")
    else:
        print("NO")


def main():
    t = int(input())
    for i in range(0, t):
        run()    

main()
