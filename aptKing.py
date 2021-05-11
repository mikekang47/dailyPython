import math

t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    print(math.comb(n+k,n-1))
