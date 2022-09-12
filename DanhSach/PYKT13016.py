x, y = 0, 1

def gcdExtended(a, b):
	global x, y
	if (a == 0):
		x = 0
		y = 1
		return b
	gcd = gcdExtended(b % a, a)
	x1 = x
	y1 = y
	x = y1 - (b // a) * x1
	y = x1
	return gcd

def modInverse(a, m):

	g = gcdExtended(a, m)
	if (g != 1):
		print(-1)
	else:
		res = (x % m + m) % m
		print(res)

a = 3
m = 5
modInverse(a, m)
