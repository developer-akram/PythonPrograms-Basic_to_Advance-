""""

r" read  ~Default
"w" write
"X" run if not exist otherwise not
"a" append add lines to the files
"t" text mode ~default
"b" binary mode
"+" read and write

"""

f = open("khanstar.txt", "r")
print(f.readlines())
# content = f.read()
# print(content)
# content = f.read(3)
# print(content)
# for reads in f :
f.close()