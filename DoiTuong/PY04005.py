import math
import sys
class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def isTriangle(self):
        return self.x1 * (self.y2 - self.y3) + self.x2 * (self.y3 - self.y1) + self.x3 * (self.y1 - self.y2) != 0.0

    def perimeter(self):
        p1, p2, p3 = [self.x1, self.y1], [self.x2, self.y2], [self.x3, self.y3]
        return math.dist(p1, p2) + math.dist(p2, p3) + math.dist(p1, p3)

a = []
for line in sys.stdin:
    for x in line.split():
        a.append(x)
t = int(a[0])
i = 1
while t > 0:
    x1, y1, x2, y2, x3, y3 = float(a[i]), float(a[i+1]), float(a[i+2]), float(a[i+3]), float(a[i+4]), float(a[i+5])
    nmc = Triangle(x1, y1, x2, y2, x3, y3)
    if nmc.isTriangle():
        print("%.3f" % (nmc.perimeter()))
    else:
        print("INVALID")
    t -= 1
    i += 6