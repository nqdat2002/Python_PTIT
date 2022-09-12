class SinhVien:
    def __init__(self, ma, hoTen, lop):
        self.ma = ma
        self.hoTen = hoTen
        self.lop = lop
        self.diem = 10

    def tinhDiem(self, txt):
        for i in range(len(txt)):
            c = txt[i]
            if c == 'v':
                self.diem -= 2
            elif c == 'm':
                self.diem -= 1
    
    def display(self):
        res = ""
        if self.diem <= 0:
            res = "0 KDDK"
        else:
            res = self.diem
        print(f"{self.ma} {self.hoTen} {self.lop} {res}")
        
n = int(input())
maSV = []
sVien = {}
for i in range(n):
    ma = input()
    maSV.append(ma)
    sv = SinhVien(ma, input(), input())
    sVien[ma] = sv

for i in range(n):
    a = [str(i) for i in input().split()]
    sv = sVien[a[0]]
    sv.tinhDiem(a[1])

for i in maSV:
    sVien[i].display()
