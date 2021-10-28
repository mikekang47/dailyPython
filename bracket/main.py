num = int(input())

for _ in range(num):
    stack = []
    p = list(str(input()))
    for a in p:
        if len(stack) == 0:
            stack.append(a)
        else:
            if a == '(':
                stack.append(a)
            else:
                if stack[-1] == '(':
                    stack.pop(-1)
                else:
                    stack.append(a)

    if len(stack) == 0:
        print("YES")
    else:
        print("NO")