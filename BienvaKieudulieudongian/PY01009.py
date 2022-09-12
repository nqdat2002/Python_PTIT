def run():
    s = input()
    dem = 0
    for i in s:
        if i.islower():
            dem = dem + 1
    if dem >= len(s) - dem:
        print(s.lower())
    else:
        print(s.upper())

run()
