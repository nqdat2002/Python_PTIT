def run():
    n = input()
    s = input()
    a = s.split()
    dem = 0
    for i in range(len(a)):
        for j in range(i):
            if int(a[j]) > int(a[i]):
                dem = dem + 1
    print(dem)

run()
