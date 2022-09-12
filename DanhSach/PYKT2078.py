import os
def sol():
    n, K = map(str, input().split())
    K = int(K)
    bits = []

    x = int(n)
    while x > 0:
        bits.append(x % 2)
        x //= 2
        
    if len(bits) == 0:
        bits.append(0)
        
    bits.reverse()
    n = [0]*(len(bits) + 1)
    ind =1
    for i in range(0, len(bits)):
        n[ind] = bits[i]
        ind +=1
        
    f = []
    for i in range(34):
        f.append([])
        for j in range(2):
            f[i].append([])
            for k in range(34):
                f[i][j].append([])
                for l in range(2):
                    f[i][j][k].append(0)

    if K > len(bits):
        print(0)
        return

    f[0][0][0][0] = 1
    for i in range(len(bits)):
        for lower in range(2):
            for k in range(i+1):
                for positive in range(2):
                    for digit in range(2):
                        cur = f[i][lower][k][positive]
                        if cur == 0:
                            continue
                        if lower == 0 and digit > n[i+1]:
                            continue
                        lower2 = lower or digit < n[i+1]
                        k2 = k
                        if positive > 0 and digit == 0:
                            k2 += 1
                        positive2 = positive or digit == 1

                        f[i+1][lower2][k2][positive2] += cur

    result = 0
    for lower in range(2):
        result += f[len(bits)][lower][K][1]

    if K == 1:
        result += 1
    print(result)


if __name__ == '__main__':
    for i in range(int(input())):
        sol()