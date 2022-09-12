tong = []
hieu = []
thuong = []
for i in range(10,100):
    for j in range(10,100-i):
        tmp_str = str(i)+' + '+str(j)+' = '+str(i+j)
        tong.append(tmp_str)

for i in range(20,100):
    for j in range(10,i-9):
        tmp_str = str(i)+' - '+str(j)+' = '+str(i-j)
        hieu.append(tmp_str)

for i in range(int(input())):
    s = input()
    if s[3] == '*' or s[3] == '/':
        print('WRONG PROBLEM!')
    else:
        if s[3] == '+':
            count = 0
            for i in tong:
                tmp = 1
                for j in range(len(s)):
                    if s[j].isdigit() and s[j] != i[j]:
                            tmp = 0
                            break
                if tmp == 1:
                    print(i)
                    count = 1
                    break
            if count == 0:
                print('WRONG PROBLEM!')
        elif s[3] == '-':
            count = 0
            for i in hieu:
                tmp = 1
                for j in range(len(s)):
                    if s[j].isdigit() and s[j] != i[j]:
                            tmp = 0
                            break
                if tmp == 1:
                    print(i)
                    count = 1
                    break
            if count == 0:
                print('WRONG PROBLEM!')
        else:
            count = 0
            if count == 0:
                for i in tong:
                    tmp = 1
                    for j in range(len(s)):
                        if s[j].isdigit() and s[j] != i[j]:
                                tmp = 0
                                break
                    if tmp == 1:
                        print(i)
                        count = 1
                        break

            if count == 0:            
                for i in hieu:
                    tmp = 1
                    for j in range(len(s)):
                        if s[j].isdigit() and s[j] != i[j]:
                                tmp = 0
                                break
                    if tmp == 1:
                        print(i)
                        count = 1
                        break
            if count == 0:
                print('WRONG PROBLEM!')