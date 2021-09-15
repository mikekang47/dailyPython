import math
import numpy as np

# a = int(input())
# r = int(input()) * 0.01
# for i in range(1,4):
#    print(math.floor(a * pow((1+r),i)))

# print("온도?")
# a = int(input())
# f = (a * 9/5)+ 32
# print(f)
# print("화씨?")
# b = int(input())
# c = (b-32) * 5/9
# print(round(c,1))
#
# a = list((input()))
# print(a[0] + "만\n" + a[1] +"천\n"+a[2] + "백\n" + a[3] + "십\n" + a[4])

mylist = [23,78, 43, 11 ,94]
mylist2 = [ 9,3,76,23,81,47,39,26,78,83,14,84]
# print(max(mylist))
# print(min(mylist))

# print(np.array(mylist).mean())
print(sorted(mylist)[int((len(mylist)+1)/2-1)])
print(sorted(mylist2)[int((len(mylist2)+1)/2-1)])
