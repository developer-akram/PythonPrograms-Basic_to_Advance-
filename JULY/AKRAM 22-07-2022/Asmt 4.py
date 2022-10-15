# 4. WAP to find max char in each string in a word?
text = "i love to play football"
max = text[0]
for i in text :
    if i > max:
        max = i
print("Max character is :",max)