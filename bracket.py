n = int(input())
for i in range(n):
    put = input()
    s = []
    for j in put:
        if(len(s)==0):
            s.append(j)
        else:
            if(s[-1] != j):
                s.pop()
            else:
                s.append(j)
    if(len(s)==0):
        print("YES")
    else:
        print("NO")
    

    