class PhanSo():
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
    
    def ucln(self, a, b):
        while a*b != 0:
            if a >= b:
                a %= b
            else:
                b %= a
        return a + b
    
    def rutgon(self):
        u = self.ucln(self.tu, self.mau)
        self.tu //= u
        self.mau //= u
    def tong(self, p):
        return self.tu * p.mau + self.mau * p.tu
    def printf(self, p):
        x = self.tong(p)
        self.mau = p.mau * self.mau
        self.tu = x
        self.rutgon()
        print(f"{self.tu}/{self.mau}")
    
a, b, c, d = map(int, input().split())

p = PhanSo(a, b)
p.printf(PhanSo(c, d))