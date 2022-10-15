# def sum (a , b):
#     return a+b
# print(sum(7 ,10))
# sum = lambda a, b : a+b
# print(sum(7 ,11))

def a_first (a):
    return a[2]
a = [[20,16, 8],[11, 9, 7],[7,3,1],[2,4,33],[1,5,5]]
a.sort(key=a_first)
print(a)