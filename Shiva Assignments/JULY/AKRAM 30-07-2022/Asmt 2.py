# 2. WAP to find max char, min char in each word of a paragraph?
text = """paragraphs are the building blocks of papers 
Many students define paragraphs in terms of length"""

mytextlist = text.split(" ")
for i in mytextlist:
    i = i.strip()
    min = i[0].lower()
    max = i[0].lower()
    for j in i:
        if j.lower() > max:
            max = j
        if j.lower() < min:
            min = j
    else:
        print(f"[{min}] min <- [{i}] max -> [{max}]")