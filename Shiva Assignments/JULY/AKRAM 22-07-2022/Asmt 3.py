# 3. WAP to find the largest palindrome in String?

text = "my name is namman my madam teach me malayalam"
a = text.split(" ")
b = []
for i in a:
    if i == i[::-1]:
        b.append(i)
high = b[0]
print("Palindromes are :")
[print(i) for i in b]
for i in range (len(b)):
    if len(b[i]) > len(high):
        high = b[i]
print("Greatest palindrome : ",high)
