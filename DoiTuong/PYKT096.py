class ThiSinh:
    def __init__(self,id,ten_thi_sinh,ma_team):
        self.id = id
        self.ten_thi_sinh = ten_thi_sinh
        self.ma_team = ma_team
        self.team_truong = team[int(self.ma_team[-2:])-1]
    def __str__(self):
        return '{} {} {}'.format(self.id,self.ten_thi_sinh,self.team_truong)

team = []
a = []
for i in range(int(input())):
    ten_team = input()
    ten_truong = input()
    team.append(ten_team+' '+ten_truong)
for i in range(int(input())):
    ten = input()
    ma = input()
    thisinh = ThiSinh('C%03d'%(i+1),ten,ma)
    a.append(thisinh)
a = sorted(a,key = lambda x: x.ten_thi_sinh)
for i in a: print(i)