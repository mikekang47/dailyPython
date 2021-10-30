import sys
k = int(sys.stdin.readline())
st = []
for i in range(k):
    a = int(sys.stdin.readline())
    if a != 0: st.append(a)
    else: st.pop(-1)
print(sum(st))