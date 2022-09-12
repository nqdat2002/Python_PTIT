class HoaDon:
    def __init__(self, ma, ten, soLuong, donGia, chietKhau):
        self.ma = ma
        self.ten = ten
        self.soLuong = soLuong
        self.donGia = donGia
        self.chietKhau = chietKhau
        self.tongTien = self.donGia * self.soLuong - self.chietKhau
    def __str__(self):
        return "{} {} {} {} {} {}".format(self.ma, self.ten, self.soLuong, self.donGia, self.chietKhau, self.tongTien)

a = []
for i in range(int(input())):
    ma = input()
    ten = input()
    soLuong = int(input())
    donGia = int(input())
    chietKhau = int(input())
    hoaDon = HoaDon(ma, ten, soLuong, donGia, chietKhau)
    a.append(hoaDon)
a = sorted(a, key=lambda x: -x.tongTien)
for i in a: print(i)