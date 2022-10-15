# def factorial (n):
#     fact = 1
#     for i  in range (n) :
#         fact = fact * (i+1)
#     return fact
# number = int(input("Enter a number : "))
# print(factorial(number))
def fact_r (n):
    """This is a program of factorial Using Recursive Function"""
    if n==1 :
        return 1
    else :
        return n * fact_r(n-1)
# 5 * fact_r(5)
# 5 * 4 * fact_r(3)
# 5 *4 * 3 * fact_r(2)
# 5 * 4 * 3 * 2 * fact_r(1)
# 5 * 4 * 3 * 2 * 1 = 120
number = int(input("Enter a Number : "))
print("Answer =",fact_r(number))
# print(fact_r.__doc__)