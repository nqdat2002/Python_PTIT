
def compress(s):
    s1 = ''
    s2 = ''
    for i in range(0, len(s)//2):
        s1 = s1 + s[i]
    for i in range(len(s)//2, len(s)):
        s2 = s2 + s[i]
    return str(int(s1) + int(s2))
s = input()
while len(s) > 1:
    s = compress(s)
    print(s)