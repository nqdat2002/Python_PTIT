def run():
    P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
    count = {}
    for i in range(0, len(P)):
        count[P[i]] = i
    T = 1
    while T == 1:
        a = input()
        a = a.split()
        if a[0] == "0":
            return
        s = a[1]
        res = ""
        k = int(a[0])
        for i in range(0, len(s)):
            res = P[(count[s[i]] + k) % 28] + res
        print(res)

run()
