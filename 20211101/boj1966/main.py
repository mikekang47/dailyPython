from collections import deque

for i in range(int(input())):
    n, m = map(int, input().split())
    q = deque(map(int,input().split()))
    q.insert(m+1, 0)
    cnt = 0

    while 1:
        q.rotate(-q.index(max(q)))
        q.popleft()
        cnt += 1

        if q[0] == 0:
            break
    print(cnt)

