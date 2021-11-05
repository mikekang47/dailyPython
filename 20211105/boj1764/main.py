import sys
n, m = map(int, sys.stdin.readline().split())
lst = sys.stdin.read().split()
r = sorted(set(lst[:n]) & set(lst[n:]))
print(len(r), *r, sep='\n')