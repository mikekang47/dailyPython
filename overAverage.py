c = int(input())

for i in range(c):
    a = list(map(int, input().split()))
    n = 0
    avg = sum(a[1:])/ a[0]
    for j in a[1:]:
        if j > avg:
            n += 1
    rate = n/a[0] * 100
    print("%.3f" %rate+"%")
    