def run():
    s = input()[::-1]
    res = ""
    for i in range(0, len(s)):
        res = s[i] + res
        if i % 3 == 2:
            res = "," + res
    print(res.lstrip(','))
    

run()

