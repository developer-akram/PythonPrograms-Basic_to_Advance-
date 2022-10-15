#5. Write a program to check divisibility of 3,5,9 with all combination.

num = int(input("Enter a number : "))

if num % 3 == 0 :
    print(num," is divisible by 3")
if num % 5 == 0 :
    print(num," is divisible by 5")
if num % 9 == 0 :
    print(num," is divisible by 9")
