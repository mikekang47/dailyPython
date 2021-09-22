def recursion(y):
    if (y < 10):
        return y
    else:
        return recursion(y % 10) + recursion(y // 10)
def solution(x):
    if (x % recursion(x) == 0):
        return True
    else:
        return False
