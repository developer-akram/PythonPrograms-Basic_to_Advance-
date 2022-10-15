#-----------------------------------------ASSIGNMENT 11--------------------------------------------------
# Q. If a five-digit number is input through the keyboard, write a
# program to print a new number by adding one to each of its
# digits. For example if the number that is input is 12391 then
# the output should be displayed as 23402.

user_input = int(input("Enter a five digit number : "))
a1 = user_input % 10
b1 = user_input // 10
a2 = b1 % 10
b2 = b1 // 10
a3 = b2 % 10
b3 = b2 // 10
a4 = b3 % 10
b4 = b3 // 10

user_output = ((b4+1)%10)*10000 + ((a4+1)%10)*1000 + ((a3+1)%10)*100 + ((a2+1)%10)*10 + ((a1+1)%10)
print("Input number  = {0}\nOutput number = {1}".format(user_input,user_output))