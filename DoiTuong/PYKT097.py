import re
ketqua = []
while(True):
    try:
        s = input()
        if s!='':
            dau = []
            tmp = s.lower().split()
            str = ' '.join(tmp)
            str_split = re.split('[.?!]',str)
            # List chứa dấu
            for i in str:
                if i == '.' or i == '?' or i == '!':
                    dau.append(i)
            # Thêm dấu chấm vào cuối nếu không đủ số dấu        
            while (len(dau)<len(str_split)):
                dau.append('.')
            # Lần lượt thêm dấu vào các phần tử list tương ứng
            vt = 0
            for i in str_split:
                if i!='':
                    i = i.strip()
                    i = i[0].upper() + i[1:] 
                    chuoi = (i+dau[vt])
                    chuoi = chuoi.strip()
                    vt += 1
                    ketqua.append(chuoi)
    except: break
for i in ketqua:
    print(i)