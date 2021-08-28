cnt = 0
for _ in range(int(input())):
    s = input()
    cnt += list(s) == sorted(s, key=s.find)
print(cnt)