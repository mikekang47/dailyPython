for _ in range(int(input())):
    s = ''
    a, b = input().split()
    for i in b:
        s+=i*int(a)
    print(s)
