#------------------------------------------------ASSIGNMENT 3-------------------------------------------------
# xercise 3: Convert Decimal number to octal using print() output formatting

user_input = int(input("Enter any binary number : "))
i = 10
a = 0
while(user_input > 0):
    a = a + (user_input % 8) * i
    user_input  = user_input // 8
    i = i * 10
user_output = a // 10
print("The octal number = ",user_output)