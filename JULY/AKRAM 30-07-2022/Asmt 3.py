# 3. WAP to validate Internet URL?

url = input("Enter any website : ")
if "www." not in url:
    url = "www."+url
mylist = url.split(".")
if len(mylist) < 3 or len(mylist[1]) < 2 or len(mylist[2]) < 2:
    print("Invalid website ")
elif len(mylist) > 3:
    if len(mylist[1]) < 2 or len(mylist[2]) < 2 or len(mylist[3]) < 2:
        print("Invalid website ")
else:
    print("Valid Website :",url)