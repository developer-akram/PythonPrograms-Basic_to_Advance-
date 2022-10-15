# 8. How to remove characters from the first String which are present in the second String?

first = "akram khan is a good boy"
second = "khan is good for a title"
print("String 1 :",first)
print("String 2 :",second)
a = first.split(" ")
b = second.split(" ")
for i in b:
    if i in a:
        a.remove(i)
print("Result :",end=" ")
[print(i,end=" ") for i in a]