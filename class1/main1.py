def printstr(str):
    return f"This is first Sentence,Understand {str}?"

def wrong_add(num1 , num2):
    return num1 + num2 -1
print("This is from ",__name__)
if __name__ == '__main__':
    # a = printstr("Akram")
    print(printstr("Akram"))
    # add = wrong_add(5 , 10)
    print(wrong_add(5 , 10))