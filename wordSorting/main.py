arr = list(set(input() for x in range(int(input()))))
arr.sort()
arr.sort(key=len)
for i in arr:
    print(i)