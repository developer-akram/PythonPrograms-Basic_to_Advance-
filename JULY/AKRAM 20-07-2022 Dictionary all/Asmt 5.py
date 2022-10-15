# 5. WAP to convert Multi dimension Dictionary to Set?

a = {"a": {"a1": 10, "a2": 20}, "b": {"b1": 100, "b2": 200}}
print("Given Dictionary :",a)
s1 = set()
s2 = set()
s3 = set()
for i, j in a.items():
    s1.add(i)
    for k,v in j.items():
        s2.add(k)
        s3.add(v)
print("Dictionary to Set :",s1,s2,s3)