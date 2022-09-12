n = int(input())
A = []
for i in input().split():
	if len(A) == 0:
		A.append(int(i))
	else:
		if (A[-1] + int(i)) % 2 == 0:
			A = A[:-1]
		else:
			A.append(int(i))
print(len(A))