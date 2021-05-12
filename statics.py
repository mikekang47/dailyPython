from statistics import *
n = int(input())
l = []
for _ in range(n):
    l.append(int(input()))
print('%.0f'%mean(l), median(l), sorted(multimode(l))[:2][-1],max(l)-min(l))