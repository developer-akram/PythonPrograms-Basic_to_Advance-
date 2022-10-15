
import extensions as file

choice = int(input("[1] print files without \n[2] print files with extension \nEnter your choice: "))
file.displayfiles(choice)
while True:
    name = input("\nType a filename with extension to find in list : ")
    file.searchfile(name)
    more = input("Enter 'm' to seach more files or press any key to exit... : ")
    if more == "m":
        continue
    else:
        break