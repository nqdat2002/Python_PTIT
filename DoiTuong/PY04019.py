# class nhanVien:
#     def __init__(self, ma, hoTen, diemLT, diemTH):
#         self.ma = ma 
#         self.hoTen = hoTen
#         self.diem = (diemLT + diemTH) / 2
    
#     def display(self):
#         d = self.diem
#         res = ""
#         if d < 5:
#             res = "TRUOT"
#         elif d < 8:
#             res = "CAN NHAC"
#         elif d < 9.5:
#             res = "DAT"
#         else:
#             res = "XUAT SAC"
#         diem = "%.2f"%(d)
#         print(f"{self.ma} {self.hoTen} {diem} {res}")

        
# def xuLiDiem(n):
#     tmp = float(n)
#     res = ""
#     if tmp > 10:
#         res = n[0:1] + "." + n[1:]
#     else:
#         res = n
#     return res


# t = int(input())
# nv = []
# for i in range(t):
#     ten = input()
#     diemLT = float(xuLiDiem(input()))
#     diemTH = float(xuLiDiem(input()))
#     ma = "TS{:02d}".format(i + 1)
#     nv.append(nhanVien(ma, ten, diemLT, diemTH))

# nv.sort(key = lambda x: -x.diem)

# for i in nv:
#     i.display()

class ThiSinh:
    def __init__(self, ma, ten, ly_thuyet, thuc_hanh):
        self.ma = ma
        self.ten = ten

        if ly_thuyet > 10:
            ly_thuyet = ly_thuyet / 10
        self.ly_thuyet = ly_thuyet

        if thuc_hanh > 10:
            thuc_hanh = thuc_hanh / 10
        self.thuc_hanh = thuc_hanh

        self.diemtb = (self.ly_thuyet + self.thuc_hanh)/2

        if self.diemtb < 5:
            self.loai = "TRUOT"
        elif self.diemtb < 8:
            self.loai = "CAN NHAC"
        elif self.diemtb <= 9.5:
            self.loai = "DAT"
        else:
            self.loai = "XUAT SAC"

    def output(self):
        return "{} {} {:.2f} {}".format(self.ma, self.ten, self.diemtb, self.loai)


if __name__ == '__main__':
    t = int(input())
    a = []
    for i in range(t):
        ts = ThiSinh("TS0" + str(i+1), input(), float(input()), float(input()))
        a.append(ts)
        t -= 1
    a.sort(key=lambda x: x.diemtb, reverse=True)
    for i in range(len(a)):
        print(a[i].output())