# -------------------------------MAP----------------------------------
# numbers = ["10","12","7","1"]
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
# numbers = list(map(int, numbers))
# numbers[2] = numbers[2] +10
# print(numbers[2])

# def square (a):
#     return a*a
# sq = list(map(square ,numbers))
# print(sq)
# or
# sq = list(map(lambda x : x*x,numbers))
# print(sq)
#
# def cube(a):
#     return a*a*a
#
# ans = [square, cube]
#
# for i in range (5):
#     ab = list(map(lambda x:x(i) ,ans))
#     print(ab)
# -------------------------------FILTER----------------------------------
# def num_g_5 (a):
#     return a>5
# fil_greater = list(filter(num_g_5, numbers))
# # name = list(if it containtslist) so list(filter(Function name(no braces), list name))
# print(fil_greater)
# -------------------------------REDUCE----------------------------------
from functools import reduce
list1 = [5,10,15,20]
num = reduce(lambda x,y:x+y, list1)
# num = 0
# for i in list1:
#     num = num + i
print(num)