# 10. How to reverse a given String?

text = input("Enter a string : ")
for i in range(len(text)-1,-1,-1):
    print(text[i],end="")