num = []
for i in range(9):
    value = int(input())
    num.append(value)
print(max(num))
print(num.index(max(num))+1)
