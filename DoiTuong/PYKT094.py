class NhanVien:
    def __init__(self,ma,ten,luong_co_ban,so_ngay_cong):
        self.ma = ma
        self.ten = ten
        self.luong_co_ban = luong_co_ban
        self.so_ngay_cong = so_ngay_cong
        # Tìm phòng
        self.phong_ban = phong[self.ma[3:]]
        self.he_so_luong = 1
    def tinhHeSoLuong(self):
        nhom = self.ma[0]
        nam = int(self.ma[1:3])
        if nhom == 'A': 
            if nam in range(1,4): self.he_so_luong = 10
            if nam in range(4,9): self.he_so_luong = 12
            if nam in range(9,16): self.he_so_luong = 14
            if nam >= 16: self.he_so_luong = 20
        if nhom == 'B':
            if nam in range(1,4): self.he_so_luong = 10
            if nam in range(4,9): self.he_so_luong = 11
            if nam in range(9,16): self.he_so_luong = 13
            if nam>=16: self.he_so_luong = 16
        if nhom == 'C':
            if nam in range(1,4): self.he_so_luong = 9
            if nam in range(4,9): self.he_so_luong = 10
            if nam in range(9,16): self.he_so_luong = 12
            if nam>=16 : self.he_so_luong = 14   
        if nhom == 'D':
            if nam in range(1,4): self.he_so_luong = 8
            if nam in range(4,9): self.he_so_luong = 9
            if nam in range(9,16): self.he_so_luong = 11
            if nam>=16: self.he_so_luong = 13
    def tinhLuong(self):
        self.luong = self.luong_co_ban * self.so_ngay_cong * self.he_so_luong * 1000
    def __str__(self):
        return '{} {} {} {}'.format(self.ma,self.ten,self.phong_ban,self.luong)
        
a = []
phong = {}
for i in range(int(input())):
    x = input()
    ma_phong = x[:2]
    ten_phong = x[3:]
    phong[ma_phong] = ten_phong
for i in range(int(input())):
    ma = input()
    ten = input()
    luong_co_ban = int(input())
    so_ngay_cong = int(input())
    nhanvien = NhanVien(ma,ten,luong_co_ban,so_ngay_cong)
    nhanvien.tinhHeSoLuong()
    nhanvien.tinhLuong()
    a.append(nhanvien)
for i in a: print(i)