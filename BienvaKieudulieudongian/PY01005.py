def run():
    s = input()
    dem = 0
    for i in s:
        if i == '4' or i == '7':
            dem = dem + 1
    if dem == 4 or dem == 7:
        print("YES")
    else:
        print("NO")

run()