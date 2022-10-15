
myfiles = ["akram.jpg","google.png","photo.jpeg","meme.gif","none.hpg",
           "mukesh.jpeg","logo.png","star.png","love.gif"]
mydict = {}
for i in myfiles:
    f = i.split(".")
    mydict.update({f[0]:f[1]})
def displayfiles(choice):
    for i in myfiles:
        if choice == 1:
            x = i.split(".")
            print(x[0],end="  ")
        elif choice == 2:
            print(i,end="  ")
        else:
            print("Invalid input")
            break
def searchfile(filename):
    if filename in myfiles:
        print(f"True, {filename} present in the list")
    else:
        m = filename.split(".")
        if m[0] in mydict.keys():
            key = m[0]
            print(f"Oops! You type {filename} with wrong extension i.e.,'{m[1]}'")
            print(f"The right filename is {key}.{mydict[key]}")
        else:
            print(f"False, {filename} not present in the list")