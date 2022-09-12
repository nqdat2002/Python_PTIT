def totient(n):
    r = 1
    p = 3
    if n % 2 == 0:
        n //= 2
    while n % 2 == 0:
        r *= 2
        n //= 2
    while p * p <= n:
        if n % p == 0:
            r *= (p - 1)
            n //= p
        while n % p == 0:
            r *= p
            n //= p
        p += 2
    if n >= 2:
        r *= (n - 1)
    return r

def power2(a, b, mx):
    if b == 0:
        return 1 % mx
    if b == 1:
        return a % mx
    tmp = power2(a, int(b // 2)) % mx
    if b % 2 == 1:
        return (((tmp % mx) * (tmp) % mx) % mx * (a % mx)) % mx
    return ((tmp % mx) * (tmp % mx)) % mx

def power(a, b, mod):
    if b == 0:
        return 1 % mod
    if b == 1:
        return a % mod
    tmp = power(a, int(b//2), mod) % mod
    if b % 2 == 1:
        return (((tmp % mod) * (tmp) % mod) % mod * (a % mod)) % mod
    return ((tmp % mod) * (tmp % mod)) % mod

def modpower(p, z, b, c, m, mx):
    cp = 0
    while m % p == 0 and cp < z:
        cp += 1
        m //= p
    t = totient(m)
    ex = ((power(b, c, t) * z) % t + t - (cp % t)) % t
    return power2(p, cp, mx) * power(p, ex, m)

def main():
    t = int(input())
    while t > 0:
        t -= 1
        a, b, c, d, m = (input().split())
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        m = int(m)
        mx = m
        a %= m
        n = totient(m)
        b %= n
        c %= n
        k = totient(n)
        d %= k
        if m == 1:
            print(0)
            continue
        if b == 0:
            print(1 % m)
            continue
        if d == 0:
            c = 1
            d = 1
        if c == 0:
            print(1 % m)
            continue
        if a == 0:
            print(0)
            continue;
        res = 1
        p = 3
        cp = 0
        while a % 2 == 0:
            a //= 2
            cp += 1
        if cp != 0:
            tmp = modpower(2, cp, c, d, m, mx)
            res *= tmp
            res %= m
        while p * p <= a:
            cp = 0
            while a % p == 0:
                a //= p
                cp += 1
            if cp != 0:
                tp = modpower(p, cp, c, d, m, mx)
                res *= tp
                res %= m  
            p += 2
        if a >= 2:
            res *= modpower(a, 1, c, d, m, mx)
            res %= m
        ans = power(res, b, m)
        print(ans % m)      
main()