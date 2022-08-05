def solve():
  s = input()
  for i in range (len (s)):
    if s[i] != '6' and s[i] != '8':
      print("NO")
      return
    if s[i] == '8':
      if i == 0 or (i == 1 and s[0] == '8' ):
        print ("NO")
        return
      if s[i - 1 : i + 1] != '68' and s[i  - 2 : i + 1] != '688':
        print ("NO")
        return
  print ("YES")

solve()