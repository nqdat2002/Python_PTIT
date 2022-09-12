mod = int(1000 * 1000 * 1000 + 7)
c = []
def Powerx(n, k):
    if k == 1:
        return n % mod
    tmp = Powerx(n, int(k / 2))
    if k % 2 == 0:
        return (tmp % mod * tmp % mod) % mod
    return (((tmp % mod * tmp % mod) % mod) * (n % mod)) % mod

def init():
    for i in range (1005):
        d = []
        for j in range (i + 1):
            d.append(0)
        c.append(d)
    for i in range(1005):
        for j in range (i + 1):
            if j == 0 or i == j:
                c[i][j] = 1
            else:
                c[i][j] = c[i - 1][j - 1] % mod + c[i - 1][j] % mod
            c[i][j] %= mod

def Load(n, k):
    if k == 0:
        return n % mod
    dp = [0] * 1005
    dp[0] = n % mod
    n %= mod
    tmp = n + 1
    for i in range (1, k + 1):
        tmp = (tmp * (n + 1) % mod) % mod
        dp[i] = (tmp - 1 + mod) % mod
        sum = 0;
        for j in range (i):
            sum = (sum % mod + (dp[j] % mod * c[i + 1][i - j + 1] % mod) % mod) % mod
        sum %= mod;
        dp[i] = (dp[i] + mod - sum) % mod
        dp[i] = dp[i] * Powerx(i + 1, mod - 2) % mod
        dp[i] %= mod
    return dp[k]

init()
t = int(input())
while t > 0:
    t -= 1
    n, k = map(int, input().split())
    res = Load(n, k)
    print(res)
