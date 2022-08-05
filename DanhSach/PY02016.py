def check(Y, a):
  for i in Y:
    if i == a:
      return 0
  return 1

def solve ():
  n = int(input())
  mylist = [int(i) for i in input().split()]
  Y = []
  res = 0
  for i in mylist:
    if(check(Y, i)):
      a = mylist.count(i)
      if a > n / 2:
        print(i)
        return
      Y.append(i)
      res += a
      if n - res < n / 2:
        print("NO")
        return
  print("NO")
      


T = int (input())

while T != 0:
  solve()
  T -= 1
