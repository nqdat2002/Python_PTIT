# https://e16cn-ptit.blogspot.com/2017/12/ptit013l-bai-l-diem-that-giao-thong.html
# Lấy code từ link trên rồi chuyển về python
road = {}
check = {}
mark = {}

def init():
    for i in range(1,n+1):
        check[i] = 0
        mark[i] = 1

def findSimilar():
    for i in range(1,n+1):
        if check[i] == 1 and mark[i] == 1:
            mark[i] = 1
        else:
            mark[i] = 0

def DQQL(r,end):
    if r == end:
        findSimilar()
    else:
        for i in range(len(road[r])):
            v = road[r][i]
            if check[v] == 0:
                check[v] = 1
                DQQL(v,end)
                check[v] = 0

for i in range(int(input())):
    # Nhập
    n, m, u, v = [int(i) for i in input().split()]
    for i in range(m):
        a, b = [int(i) for i in input().split()]
        if a in road:
            road[a].append(b)
        else:
            road[a] = [b]
    # Khởi tạo dict
    init()
    # Đệ quy
    DQQL(u,v)
    # Đếm
    check[u] = 1
    count = 0
    for i in range(1,n+1):
        if i!=u and i!=v and mark[i]==1:
            count += 1
    print(count)
    # Xoá dữ liệu trong road
    for i in road:
        road[i].clear()