# https://gialaipc.com.vn/lam-the-nao-de-lam-tron-bang-python/#phuong-phap-1-su-dung-ham-round-tich-hop-san

from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

class HocSinh:
    def __init__(self,id,ho_ten,diem_1,diem_2,diem_3):
        self.id = id
        self.ho_ten = ho_ten
        self.diem_1 = diem_1
        self.diem_2 = diem_2
        self.diem_3 = diem_3
        self.trung_binh = (self.diem_1*3.0+self.diem_2*3.0+self.diem_3*2.0)/8
        self.trung_binh = Decimal(str(self.trung_binh)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    def __str__(self):
        return '{} {} {}'.format(self.id,self.ho_ten,self.trung_binh)

a = []
trung_binh_list = []
xep_hang_list = []
for i in range(int(input())):
    tmp = input().split()
    ten = ' '.join(tmp)
    ten = ten.title()
    diem1 = int(input())
    diem2 = int(input())
    diem3 = int(input())
    hocsinh = HocSinh('SV%02d'%(i+1),ten,diem1,diem2,diem3)
    a.append(hocsinh)
a = sorted(a,key=lambda x: (-x.trung_binh,x.id))
# Đưa các giá trị trung bình vào mảng riêng rồi đánh số thứ tự cho nó như đề bài
for i in a: trung_binh_list.append(i.trung_binh)
thutu = 1
for i in range(len(trung_binh_list)-1):
    if trung_binh_list[i]==trung_binh_list[i+1]:
        xep_hang_list.append(thutu)
    else:
        xep_hang_list.append(thutu)
        thutu += trung_binh_list.count(trung_binh_list[i])
xep_hang_list.append(thutu)
# In lần lượt học sinh rồi đến số thứ tự
for i in range(len(a)):
    print(a[i],xep_hang_list[i], sep = ' ')