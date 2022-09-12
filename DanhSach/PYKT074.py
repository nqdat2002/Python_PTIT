import textwrap

T = int(input())
while T > 0:
    T -= 1
    s = input()
    res = textwrap.shorten(s, width = 100, placeholder="")
    print(res)