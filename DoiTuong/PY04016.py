import datetime
class Customer:
    def __init__(self, ma, ten, soPhong, ngayNhanPhong, ngayTraPhong, tienPhatSinh):
        self.ma = ma
        self.ten = ten.strip()
        self.soPhong = soPhong.strip()
        self.ngayNhanPhong = ngayNhanPhong
        self.ngayTraPhong = ngayTraPhong
        self.tienPhatSinh = tienPhatSinh
        self.tongTien = self.tongTien()

    def tinhNgay(self):
        d1 = self.ngayNhanPhong.split("/")
        d2 = self.ngayTraPhong.split("/")
        dt1 = datetime.datetime(int(d1[2]), int(d1[1]), int(d1[0]))
        dt2 = datetime.datetime(int(d2[2]), int(d2[1]), int(d2[0]))
        return (dt2 - dt1).days + 1
    
    def tongTien(self):
        c = self.soPhong[0]
        phi = 0
        if c == '1':
            phi = 25
        elif c == '2':
            phi = 34
        elif c == '3':
            phi = 50
        else:
            phi = 80
        return phi * self.tinhNgay() + self.tienPhatSinh

    def display(self):
        ngay = self.tinhNgay()
        print(f"{self.ma} {self.ten} {self.soPhong} {ngay} {self.tongTien}")

t = int(input())
kh = []
for i in range(t):
    ma = "KH{:02d}".format(i + 1)
    kh.append(Customer(ma, input(), input(), input(), input(), int(input())))

kh.sort(key = lambda x : -x.tongTien)
for i in kh:
    i.display()