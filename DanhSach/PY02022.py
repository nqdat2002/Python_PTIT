import math

def isPrime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    # a = sorted(a)
    count = {}
    for i in a:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    for i in a:
        if isPrime(int(i)) and count[i] != 0:
            print(i, count[i])
            count[i] = 0

main()