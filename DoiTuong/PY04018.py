class GiaoVien:
    def __init__(self, id, ten, ma, diemTin, diemCM):
        self.id = id
        self.ten = ten
        self.ma = ma
        self.diemTin = diemTin
        self.diemCM = diemCM
        self.mon = self.setMon()
        self.tongDiem = self.tinhTongDiem()

    def setMon(self):
        ma = self.ma[0]
        if ma == 'A':
            return "TOAN"
        elif ma == 'B':
            return "LY"
        return "HOA"

    def tinhTongDiem(self):
        ma = self.ma[1]
        diem = self.diemCM + self.diemTin * 2
        if ma == '1':
            diem += 2
        elif ma == '2':
            diem += 1.5
        elif ma == '3':
            diem += 1
        return diem

    def display(self):
        diem = float("{:1f}".format(self.tongDiem))
        res = ""
        if diem >= 18:
            res = "TRUNG TUYEN"
        else:
            res = "LOAI"
        print(f"{self.id} {self.ten} {self.mon} {diem} {res}")

t = int(input())
arr = []
for i in range(t):
    ma = "GV{:02d}".format(i + 1)
    arr.append(GiaoVien(ma, input(), input(), float(input()), float(input())))

arr.sort(key = lambda x: -x.tongDiem)

for i in arr:
    i.display()