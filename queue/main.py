import sys

num = int(sys.stdin.readline())
q = []

for _ in range(num):
    ar = sys.stdin.readline().split()
    if ar[0] == "push":
        q.append(ar[1])
    elif ar[0] == "pop":
        print(q.pop(0)) if q else print(-1)
    elif ar[0] == "size":
        print(len(q))
    elif ar[0] == "empty":
        print(1) if not q else print(0)
    elif ar[0] == "front":
        print(q[0]) if q else print(-1)
    elif ar[0] == "back":
        print(q[-1]) if q else print(-1)


