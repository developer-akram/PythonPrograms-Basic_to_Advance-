# 6. Write a  program to print all alphabets from a to z.
i = ord("a")
# print(ord("z"))
print("All alphabets in small letters : ")
while i <= ord("z"):
    print(chr(i),end=" ")
    i += 1
print("\nAll alphabets in Block letters")
i = ord("A")
while i <= ord("Z"):
    print(chr(i),end=" ")
    i += 1
