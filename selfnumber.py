num = []
for i in range(9999):
    num.append(i + sum([int(x) for x in str(i)]))
for i in range(9999):
    if i not in num:
        print(i)