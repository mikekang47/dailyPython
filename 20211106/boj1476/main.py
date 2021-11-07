import sys

e, m, s = map(int, sys.stdin.readline().split())
year = 0
while 1:
    year += 1
    E = year % 15
    M = year % 28
    S = year % 19
    if E == 0:
        E = 15
    if M == 0:
        M = 28
    if S == 0:
        S = 19

    if E == e and S == s and M == m:
        break

print(year)
