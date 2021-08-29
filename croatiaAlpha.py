alpha = ["c=", "c-", "d-", "dz=", "lj", "nj", "s=", "z="]
cnt = 0
s = str(input())
for i in alpha:
    s = s.replace(i," ")
cnt += len(s)
print(cnt)