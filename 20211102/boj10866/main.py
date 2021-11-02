from collections import deque
import sys
dq = deque()

for _ in range(int(input())):
    ipt = list(sys.stdin.readline().split())
    first = ipt[0]
    if first == "push_back":
        dq.append(ipt[1])
    elif first == "push_front":
        dq.appendleft(ipt[1])
    elif first == "pop_front":
        if len(dq) != 0:
            print(dq.popleft())
        else:
            print("-1")
    elif first == "pop_back":
        if len(dq) != 0:
            print(dq.pop())
        else:
            print("-1")
    elif first == "size":
        print(len(dq))
    elif first == "empty":
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    elif first == "front":
        if len(dq) != 0:
            print(dq[0])
        else:
            print("-1")
    elif first == "back":
        if len(dq) != 0:
            print(dq[-1])
        else:
            print("-1")


