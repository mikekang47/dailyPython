from collections import *

deque_list = deque()
for i in range(5):
    deque_list.append(i)
print(deque_list)
deque_list.pop()
deque_list.append(10)
print(deque_list)