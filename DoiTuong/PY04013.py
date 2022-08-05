dic = {}

n = int(input())

for i in range(n):
    name = input()
    start = input().split(':')
    st = int(start[0]) * 60 + int(start[1])

    end = input().split(':')
    ed = int(end[0]) * 60 + int(end[1])
    mua = int(input())
    try:
        (dic[name])[0] += ed - st
        (dic[name])[1] += mua
    except:
        dic.update({name : [0, 0]})
        (dic[name])[0] += ed - st
        (dic[name])[1] += mua

dem = 0
for key, value in dic.items():
    dem += 1
    print('T{:02d}'.format(dem), key, '{:.2f}'.format(value[1]*60/ value[0]))

'''
10
Dong Anh
07:30
08:00
60
Cau Giay
07:45
08:12
50
Soc Son
08:00
09:15
78
Dong Anh
18:50
20:00
88
Cau Giay
19:01
20:00
77
Soc Son
19:06
20:21
66
Dong Anh
21:00
21:40
49
Cau Giay
21:50
22:20
68
Dong Anh
22:15
23:45
30
Cau Giay
22:50
23:45
35
'''