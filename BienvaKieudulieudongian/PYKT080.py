l =[]
q = []
b = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
n, m = map(int, input().split())
for i in range(n):
    l.append(list(int(x) for x in input().split()))
    for j in range(m):
        if l[i][j] == -1:
            q.append([i,j])
dem = 0
while len(q) > 0:
    u = q[0]
    q.pop(0)
    for i in b:
        ii, jj = i[0]+u[0], i[1]+u[1]
        if ii >= 0 and ii < n and jj >= 0 and jj < m:
            if l[ii][jj] != 0:
                dem += l[ii][jj]
                l[ii][jj] = 0
print(dem)