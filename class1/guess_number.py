#i = 18
gnum = 9
guess = 0
while(True) :
    print("Number off guesses left : ", gnum)
    gnum = gnum - 1
    num1 = int(input("Guess a number between 1 to 100 : "))
    guess = guess + 1
    if num1 >= 100 and gnum >0 or num1<1:
        print("Invalid Choice.Choose a number between 1 to 100")
        continue
    elif num1>18 and gnum>0:
        print("Your guess is too high\t",guess,"guess used")
        continue
    elif num1<18 and gnum>0:
        print("Your guess is too low\t",guess,"guess used")
        continue
    elif num1 == 18 and gnum>0:
        print("Congrats.You have successfully guess the correct number in",guess,"guess")
        break

    else:
        print("GAME OVER")
        break