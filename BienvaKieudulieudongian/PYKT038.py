s = input()
ans = ''
for i in range(len(s) - 3, -1, -3):
    tmp = s[i : i + 3]
    # print(tmp)
    ans = str(int(tmp[0]) * 4 + int(tmp[1]) * 2 + int(tmp[2])) + ans
if len(s) % 3 == 1:
    ans = s[0] + ans
elif len(s) % 3 == 2:
    ans = str(int (s[0]) * 2 + int(s[1])) + ans
print(ans)