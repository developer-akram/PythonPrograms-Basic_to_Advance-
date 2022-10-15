list1 = ["Banana","Bhnidi","Apple","Tomato","Orange","Potato","Kaju","Karela"]
# i=1
# for item in list1 :
#     if i%2 == 1 :
#         print("Fruits name :",item)
#     i+=1
for key,value in enumerate(list1):
    if key%2 == 1:
    #     print (f"Fruits are {value}")
    # # else :
        print(f"Vegetables are {value}")