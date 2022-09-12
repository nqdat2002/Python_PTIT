def check(str):
    for i in str:
        if(int(i) % 2 == 1):
            return False
    return True

t = int(input())
for i in range(t):
    n = int(input())
    for i in range(22, n, 2):
        txt = str(i)
        if(len(txt) % 2 == 1):# khi i chạy đến 100 hay 10000(tức là len lẻ), ta cộng với 900 hay 90000 để len chẵn trở lại => không cần lặp qua các i có len lẻ
            i += 9 * len(txt)
            txt = str(i)
        if((txt == txt[::-1])):
                if(check(txt)):
                    print(i,end = " ")
    print()           
# # cách 2
# def gen(stri):
#     for i in range(0,9,2):
#         char = str(i)
#         tmp = char + stri + char
#         a.append(tmp)
#         if len(tmp) < 6:
#             gen(tmp)

# a = []
# gen("")
# b = []
# for i in range (len(a)):
#     if a[i][0] != '0':
#         b.append(a[i])
# b = [int(i) for i in b]
# b.sort()

# t = int(input())
# while t > 0:
#     t -= 1
#     n = int(input())
    
#     for i in b:
#         if i < n:
#             print(i, end=" ")
#     print()             