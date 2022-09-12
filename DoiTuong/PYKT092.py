class ThiSinh:
    def __init__(self,id,ho_ten,diem_thi,dan_toc,khu_vuc):
        self.id = id
        self.ho_ten = ho_ten
        self.diem_thi = diem_thi
        self.dan_toc = dan_toc
        self.khu_vuc = khu_vuc
        self.diem_uu_tien = 0.0
    def tinhDiem(self):
        if self.khu_vuc == 1: self.diem_uu_tien += 1.5
        elif self.khu_vuc == 2: self.diem_uu_tien += 1
        if self.dan_toc != 'Kinh': self.diem_uu_tien += 1.5
        self.diem_thi += self.diem_uu_tien
        if self.diem_thi >= 20.5: self.trang_thai = 'Do'
        else: self.trang_thai = 'Truot'
    def __str__(self):
        return '{} {} {} {}'.format(self.id,self.ho_ten,self.diem_thi,self.trang_thai)

a = []
for i in range(int(input())):
    # Nhập tên rồi chuẩn hoá
    ten = input().split()
    ten_chuan_hoa = ' '.join(ten)
    ten_chuan_hoa = ten_chuan_hoa.title()
    diem_thi = float(input())
    dan_toc = input()
    khu_vuc = int(input())
    thisinh = ThiSinh('TS%02d'%(i+1),ten_chuan_hoa,diem_thi,dan_toc,khu_vuc)
    thisinh.tinhDiem()
    a.append(thisinh)
a = sorted(a,key=lambda x: (-x.diem_thi,x.id))
for i in a: print(i)