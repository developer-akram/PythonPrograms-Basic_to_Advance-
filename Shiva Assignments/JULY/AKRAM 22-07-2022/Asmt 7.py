# 7. How to remove all duplicates from a given string?

text = "two and two doesn't make two because two and two make four"
print(text)
a = text.split(" ")
b = []
for i in a:
    if i not in b:
        b.append(i)
[print(i,end=" ") for i in b]
