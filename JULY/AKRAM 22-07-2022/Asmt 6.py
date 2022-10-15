# 6. WAP to reverse a string in words?

text = "C CPP DS Java PHP"
print(text)
a = text.split(" ")
for i in a:
    print(i[::-1],end=" ")