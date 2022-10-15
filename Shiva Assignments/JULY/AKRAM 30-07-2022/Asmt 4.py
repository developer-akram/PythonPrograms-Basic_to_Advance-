# 4. WAP to find maximum length palindrome in a paragraph?

text = """my name is namman my madam teach me malayalam 
abcxyzzyxcba is rootoor given to my targets"""
a = text.split(" ")
b = []
for i in a:
    i = i.strip()
    if i == i[::-1]:
        b.append(i)
high = b[0]
print("Palindromes are :")
[print(i) for i in b]
for i in range (len(b)):
    if len(b[i]) > len(high):
        high = b[i]
print("Greatest palindrome : ",high)