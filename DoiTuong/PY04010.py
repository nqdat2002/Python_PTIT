class ThiSinh():
    def __init__(self, name, date, mon1, mon2, mon3):
        self.name = name
        self.date = date
        self.mon1 = mon1
        self.mon2 = mon2
        self.mon3 = mon3
        self.tongdiem = mon1 + mon2 + mon3
    
    def printf(self):
        print(self.name, self.date, '{:.1f}'.format(self.tongdiem))
    

name = input()
date = input()
mon1 = float(input())
mon2 = float(input())
mon3 = float(input())

ThiSinh(name, date, mon1, mon2, mon3).printf()
