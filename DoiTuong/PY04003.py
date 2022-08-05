from math import gcd

class PhanSo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def toiGian(self):
        m = gcd(self.x, self.y)
        print(f"{self.x // m}/{self.y // m}")
    
s = [int(i) for i in input().split()]
p = PhanSo(s[0], s[1])
p.toiGian()