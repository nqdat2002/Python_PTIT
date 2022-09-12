import math
a = float(4 * math.sqrt(3) + 4)

s = float(input())
b = 4 * math.sqrt(s)
x1 = ((-b + math.sqrt(b * b + 4 * s * a)) / (2 * a))
print("{:.4f}".format(x1))