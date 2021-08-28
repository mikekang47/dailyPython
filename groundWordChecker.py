cnt = 0
for i in range(input()):
    s = input()
    cnt += list(s) == sorted(s, key=s.find)
print(cnt)