n = int(input())
if n in [4,7]:
    print(-1)
else :
    print(n //5 + n%5 - n%5//3*2)