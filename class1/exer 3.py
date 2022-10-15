# ----------------------------GUESS THE NUMBER-----------------------------
print("Wecome to the game : GUESS THE CORRECT NUMBER")
guess_left = 10
try_guess = 1
print("Number of guesses left : ",guess_left)
while (try_guess <=10 ):
    number = int(input("Guess a number between 1 to 100 : "))
    if try_guess == 10:
        print("Sorry! You have tried maximum number of guesses, GAME OVER")
        break
    if number > 18 :
        print("You tried",try_guess,"times and number of guesses left",guess_left - 1)
        print("You guess is high, Try again")
        guess_left  = guess_left - 1
        try_guess = try_guess + 1
    elif number < 18 :
        print("You tried",try_guess,"times and number of guesses left",guess_left - 1)
        print("You guess is low, Try again")
        guess_left  = guess_left - 1
        try_guess = try_guess + 1
    elif number == 18 :
        print("Congratulation! You have guess sucessfully the correct number in",try_guess,"guesses")
        break
    else :
        print("Invalid")
