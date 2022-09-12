T = int(input())
class SinhVien:
    def __init__(self, name, c, t):
        self.name = name
        self.c = c
        self.t = t
    def viet(self):
        print(self.name, self.c, self.t)

a = []
while T > 0:
    T -= 1
    s = input()
    c, t = map(int, input().split())
    sv = SinhVien(s, c, t)
    a.append(sv)

a = sorted(a, key = lambda x: (-x.c, x.t, x.name))
for i in a:
    i.viet()