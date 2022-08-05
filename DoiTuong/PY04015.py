
from decimal import ROUND_HALF_UP, Decimal


class hoadon():
    def __init__(self, ma, name, tiendien) :
        self.ma = ma
        self.name = name
        self.tiendien = tiendien
    def total(self):
        print(self.ma, self.name, self.tiendien)

n = int(input())
L = []
dem = 0
for i in range(n):
    dem += 1
    name = input()
    start = Decimal(input())
    end = Decimal(input())
    sodien = end - start
    if sodien <= 50:
        tmp = 102
    elif sodien <= 100:
        tmp = 103
    else:
        tmp = 105

    tiendien = 0
    if sodien <= 50:
        tiendien = sodien * 100
        sodien = 0
    else:
        tiendien = 100 * 50
        sodien -= 50
    if sodien <= 50:
        tiendien += sodien * 150
        sodien = 0
    else:
        tiendien += 150 * 50
        sodien -= 50
    
    tiendien += sodien * 200
    tiendien *= tmp
    tiendien = Decimal(tiendien) / Decimal(100)
    tiendien = tiendien.quantize(Decimal('1'), ROUND_HALF_UP)
    
    L.append(hoadon('KH{:02d}'.format(dem), name, tiendien))
    

L = sorted(L, key = lambda x : -x.tiendien)

for i in L:
    i.total()
'''
3
Le Thi Thanh
468
500
Le Duc Cong
160
230
Ha Hue Anh
410
612
'''
