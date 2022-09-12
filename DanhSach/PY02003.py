MAX = 10 ** 18
a = []
for i in range(0, 61):
    for j in range(0, 39):
        for k in range(0, 27):
            num = (2 ** i) * (3 ** j) * (5 ** k)
            if num <= MAX:
                a.append(num)

a.sort()
ham_sequence = dict(map(lambda x : (x, a.index(x) + 1), a))

for i in range(int(input())):
    num = int(input())
    res = ham_sequence.get(num, "Not in sequence")
    print(res)