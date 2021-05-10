x = input().upper()
m = 0
for i in set(x):
    t = x.count(i)
    if t == m:
        r="?"
    elif t==max(t,m):
        r=i
    m=max(t,m)
print(r)