class MonThi:
    def __init__(self, ma, ten, hinhthuc):
        self.ma = ma
        self.ten = ten
        self.hinhthuc = hinhthuc
    def printf(self):
        print(self.ma, self.ten, self.hinhthuc)

n = int(input())
L = []
for i in range(n):
    ma = input().strip()
    name = input().strip()
    hinhthuc = input().strip()
    L.append(MonThi(ma, name, hinhthuc))

L = sorted(L, key=lambda x : x.ma)
for i in L:
    i.printf()

