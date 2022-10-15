# 1. WAP to count total repeated words in a paragraph

a = """Hello mam i am good mam and mam how are you 
Hello mukesh i am doing my homework and mukesh what about you"""
mylist = a.split(" ")
mydict = {}
for i in mylist:
    if i in mydict.keys():
        continue
    else:
        value = a.count(i)
        if value > 1:
            mydict.update({i:value})
print("Input Sentence :\n",a)
for i,j in mydict.items():
    print(f"[{i}] occurs [{j}] times")






