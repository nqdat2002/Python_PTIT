class VanDongVien:
    def __init__(self, hoTen, donVi, tgianDen):
        self.hoTen = hoTen
        self.donVi = donVi
        self.tgianDen = tgianDen
        self.vt = self.tinhVanToc()
        self.ma = self.setMa()

    def setMa(self):
        res = ""
        dv = self.donVi.split()
        for i in dv:
            res += i[0]
        ht = self.hoTen.split()
        for i in ht:
            res += i[0]
        return res
    
    def tinhVanToc(self):
        tgian = self.tgianDen.split(":")
        tmp = (int)(tgian[0]) * 60 + int(tgian[1])
        tmp -= 6 * 60
        tmp /= 60
        return 120/tmp

    def display(self):
        vtoc = round(self.vt)
        print(f"{self.ma} {self.hoTen} {self.donVi} {vtoc} Km/h")


t = int(input())
a = []

for i in range(t):
    a.append(VanDongVien(input(), input(), input()))

a.sort(key = lambda x : -x.vt)
for i in a:
    i.display()