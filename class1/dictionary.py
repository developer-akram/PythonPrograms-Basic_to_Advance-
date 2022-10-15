d1 = {}
print(type(d1))
d2 = {"Akram":"Malahar", "Biki":"Mathurapur", "Didi":"Murshidabad",
      "Naim":"Kumarganj", "Arafat":"Harsura", "Masud":"Tapan",
      "Rahul":{"City":"Mumbai","State":"Maharastra","PIN":"500001"}}
print(d2)
"""
d2.update({"Mehedi":"Malda"})
print(d2)
d2["Lady"] = "Sonarpur"
print(d2)
print(d2.keys())
print(d2.items())
"""
del d2["Masud"]
print(d2)
d3 = d2.copy()
del d3["Akram"]
print(d2)
print(d2["Rahul"])
print(d2["Rahul"]["PIN"])
del d2["Rahul"]
print(d2)
print(d2.items())