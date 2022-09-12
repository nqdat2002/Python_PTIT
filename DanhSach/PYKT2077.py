import math
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True
def sol():
    s = input()
    n = len(s)
    digits = [int(i) for i in s]
    f = []
    for i in range(n+1):
        f.append([])
        for j in range(3):
            f[i].append([])
            for k in range(137):
                f[i][j].append([])
                for l in range(137):
                    f[i][j][k].append(0)

    f[n][0][0][0] = 1

    for i in range(n, 0, -1):
        for rem in range(0, 3):
            for sumx in range(136):
                for sumy in range(0, 136):
                    cur = f[i][rem][sumx][sumy]
                    if cur == 0:
                        continue

                    for x in range(0, 10):
                        for y in range(0, 10):
                            t = x + y * 2 + rem
                            if t % 10 == digits[i-1]:
                                f[i-1][int(t/10)][sumx+x][sumy+y] += cur

    result = 0
    for sumx in range(1, 136):
        for sumy in range(1, 136):
            if isPrime(sumx) and isPrime(sumy):
                result += f[0][0][sumx][sumy]
    print(result)
    
if __name__ == "__main__":
    sol()
