def prepare(a, b):
    if (a >= 21 and b == 3) or (a <= 19 and b == 4):
        print('Bach Duong')
    if (a >= 20 and b == 4) or (a <= 20 and b == 5):
        print('Kim Nguu')
    if (a >= 21 and b == 5) or (a <= 20 and b == 6):
        print('Song Tu')
    if (a >= 21 and b == 6) or (a <= 22 and b == 7):
        print('Cu Giai')
    if (a >= 23 and b == 7) or (a <= 22 and b == 8):
        print('Su Tu')
    if (a >= 23 and b == 8) or (a <= 22 and b == 9):
        print('Xu Nu')
    if (a >= 23 and b == 9) or (a <= 22 and b == 10):
        print('Thien Binh')
    if (a >= 23 and b == 10) or (a <= 22 and b == 11):
        print('Thien Yet')
    if (a >= 23 and b == 11) or (a <= 21 and b == 12):
        print('Nhan Ma')
    if (a >= 22 and b == 12) or (a <= 19 and b == 1):
        print('Ma Ket')
    if (a >= 20 and b == 1) or (a <= 18 and b == 2):
        print('Bao Binh')
    if (a >= 19 and b == 2) or (a <= 20 and b == 3):
        print('Song Ngu')

t = int(input())

while t > 0:
    t -= 1
    a, b = map(int, input().split())
    prepare(a, b)