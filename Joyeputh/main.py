n, k = map(int, input().split())
arr = list(range(1, n+1))
ans = []

for i in range(n):
    new_k = (k-1) % len(arr)
    ans.append(arr[new_k])
    arr = arr[new_k+1:]+arr[:new_k]
print('<'+str(ans)[1:-1]+'>')

