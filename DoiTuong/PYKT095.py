class TienDien:
    def __init__(self,id,ho_ten,loai_ho_gia_dinh,chi_so_dau,chi_so_cuoi):
        self.id = id
        self.ho_ten = ho_ten
        self.loai_ho_gia_dinh = loai_ho_gia_dinh
        self.chi_so_dau = chi_so_dau
        self.chi_so_cuoi = chi_so_cuoi
        self.so_dien = chi_so_cuoi - chi_so_dau
        # Tìm định mức
        if self.loai_ho_gia_dinh == 'A':
            self.dinh_muc = 100
        elif self.loai_ho_gia_dinh == 'B':
            self.dinh_muc = 500
        else:
            self.dinh_muc = 200
        # Tính tiền trong định mức
        if self.so_dien < self.dinh_muc:
            self.tien_trong_dinh_muc = self.so_dien*450
        else:
            self.tien_trong_dinh_muc = self.dinh_muc*450
        # Tính tiền vượt định mức
        if self.so_dien > self.dinh_muc:
            self.tien_vuot_dinh_muc = (self.so_dien - self.dinh_muc)*1000
        else:
            self.tien_vuot_dinh_muc = 0
        # Tính VAT
        self.VAT = int(self.tien_vuot_dinh_muc/20)
    def tinhTongTien(self):
        self.tong_tien = self.tien_trong_dinh_muc + self.tien_vuot_dinh_muc + self.VAT
    def __str__(self):
        return '{} {} {} {} {} {}'.format(self.id,self.ho_ten,self.tien_trong_dinh_muc,self.tien_vuot_dinh_muc,self.VAT,self.tong_tien)
a = []
for i in range(int(input())):
    hoten = input().split()
    hotenxoacach = ' '.join(hoten)
    loaihogiadinh, chisodau, chisocuoi = input().split()
    giadinh = TienDien('KH%02d'%(i+1),hotenxoacach.title(),loaihogiadinh,int(chisodau),int(chisocuoi))
    giadinh.tinhTongTien()
    a.append(giadinh)
a = sorted(a,key=lambda x: x.tong_tien, reverse=True)
for i in a:
    print(i)