a = int(input())
arr = []
for _ in range(a):
    arr.append(int(input()))
st = []
output = []
idx = 0

for i in range(1, a+1):
    st.append(i)
    output.append('+')

    while len(st) != 0:
        if arr[idx] == st[-1]:
            st.pop(-1)
            output.append('-')
            idx += 1
        else:
            break;

if len(st) == 0:
    for i in output:
        print(i)

else:
    print("NO")
