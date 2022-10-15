# 15. Write a program to get the maximum and minimum value of dictionary.

a = {"abc": 7000, "bcd": 2000, "cde": 6000, "def": 4000, "efg": 5000}
print("Given Dictionary :",a)
list1 = a.values()
print("Maximum value :",max(list1))
print("Minimum value :",min(list1))