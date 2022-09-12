class Phim:
    def __init__(self,id,ma_the_loai,ngay_khoi_chieu,ten_phim,so_tap_phim):
        self.id = id
        self.ma_the_loai = ma_the_loai
        self.ngay_khoi_chieu = ngay_khoi_chieu
        self.ten_phim = ten_phim
        self.so_tap_phim = so_tap_phim
        self.the_loai = ''
    def timTheLoai(self):
        self.the_loai = list_the_loai[int(self.ma_the_loai[2:])-1]
    def __str__(self):
            return '{} {} {} {} {}'.format(self.id,self.the_loai,self.ngay_khoi_chieu,self.ten_phim,self.so_tap_phim)
            
a = []
# Nhập n, m và tạo list thể loại
so_luong_the_loai, so_luong_bo_phim = [int(i) for i in input().split()]
list_the_loai = []
for i in range(so_luong_the_loai):
    list_the_loai.append(input())
# Nhập thông tin phim
for i in range(so_luong_bo_phim):
    phim = Phim('P%03d'%(i+1),input(),input(),input(),int(input()))
    phim.timTheLoai()
    a.append(phim)
a = sorted(a,key=lambda x: x.ngay_khoi_chieu, reverse=True)
for i in a:
    print(i)