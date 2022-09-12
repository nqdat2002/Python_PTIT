import re
regex = '[\w\s,:]+'

def solve(s):
    l = re.findall(regex,s)

    for sentence in l:
        tmp = sentence.lower().split()
        tmp[0] = tmp[0].title()
        string = ' '.join(tmp)
        print(string)

s = ""
while True: 
    try: 
        s += input()
    except EOFError: 
        break
solve(s)