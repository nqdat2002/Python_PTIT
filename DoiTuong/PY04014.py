from decimal import ROUND_HALF_UP, Decimal
from fractions import Fraction

class HS():
    def __init__(self, ma, name, diem):
        self.ma = ma
        self.name = name
        self.diem = diem
    def phanloai(self):
        if self.diem >= 9.0:
            self.loai = 'XUAT SAC'
        elif self.diem >= 8.0:
            self.loai = 'GIOI'
        elif self.diem >= 7.0:
            self.loai = 'KHA'
        elif self.diem >= 5.0:
            self.loai = 'TB'
        else:
            self.loai = 'YEU'
    
    def total(self):
        self.phanloai()
        print(self.ma, self.name, self.diem, self.loai)
n = int(input())
L = []
dem = 0
for i in range(n):
    dem += 1
    name = input()
    a = [Decimal(j) for j in input().split()]
    diem = a[0] + a[1]
    for j in a:
        diem += j
    diem = Decimal(diem) / Decimal(len(a) + 2)
    diem = diem.quantize(Decimal('0.1'), ROUND_HALF_UP)
    id = 'HS{:02d}'.format(dem)
    L.append(HS(id, name, diem))

l = sorted(L, key= lambda x : (- x.diem, x.ma))
for hs in l:
    hs.total()

'''
3
Luu Thuy Nhi
9.3  9.0  7.1  6.5  6.2  6.0  8.2  6.7  4.8  5.5
Le Van Tam
8.0  8.0  5.5  9.0  6.8  9.0  7.2  8.3  7.2  6.8
Nguyen Thai Binh
9.0  6.4  6.0  7.5  6.7  5.5  5.0  6.0  6.0  6.0
'''
