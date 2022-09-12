import datetime
class LichThi:
    def __init__(self,id,ma_mon_hoc,ngay_thi,gio_thi,nhom_thi):
        self.id = id
        self.ma_mon_hoc = ma_mon_hoc
        self.ngay_thi = ngay_thi
        self.gio_thi = gio_thi
        self.nhom_thi = nhom_thi
        self.ten_mon_hoc = hoc[self.ma_mon_hoc]
        # Đổi ngày thi về đúng định dạng date thì mới so sánh và sắp xếp trong hàm bên dưới được
        self.ngay_thi_quy_doi = datetime.datetime.strptime(self.ngay_thi[:6] + self.ngay_thi[8:], '%d/%m/%y') # Phải dùng slice để cắt ngày thi về định dạng xx/yy/zz
        # Đổi giờ về đúng định dạng
        self.gio_thi_quy_doi = datetime.datetime.strptime(self.gio_thi, '%H:%M')
    def __str__(self):
        return '{} {} {} {} {} {}'.format(self.id,self.ma_mon_hoc,self.ten_mon_hoc,self.ngay_thi,self.gio_thi,self.nhom_thi)

# Nhập n, m
n, m = [int(i) for i in input().split()]
# Nhập thông tin mã môn học và tên môn học và lưu vào dict
hoc = {}
for i in range(n):
    thong_tin_ma_mon_hoc = input()
    ten_mon_hoc = input()
    hoc[thong_tin_ma_mon_hoc] = ten_mon_hoc
# Nhập lịch thi
a = []
for i in range(m):
    ma, ngay, gio, nhom = input().split()
    lichthi = LichThi('T%03d'%(i+1),ma,ngay,gio,nhom)
    a.append(lichthi)
a = sorted(a, key=lambda x: (x.ngay_thi_quy_doi,x.gio_thi_quy_doi,x.ma_mon_hoc))
for i in a: print(i)