import queue
digits = ['2', '3', '5', '7']
n = int(input())
q = queue.Queue(0)
for digit in digits:
    q.put(digit)
while not q.empty():
    curr = q.get()
    if curr[-1] != '2' and len(set(curr)) == 4:
        print(curr)
    for digit in digits:
        if len(curr) < n:
            q.put(curr + digit)