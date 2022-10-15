#Program Pasand aajay to like kr dena Comment ko Brother
import random
list1 = {"s": "Snake","w": "Water","g" : "Gun"}
list2 = ["Snake","Water","Gun"]
count = 0
c_score = 0
u_score = 0
draw = 0
max_chance = 10
print("Welcome to the game\nSNAKE WATER GUN")
while max_chance>count:
    print("Compuer Score",c_score,"\nUser    Score",u_score)
    print(max_chance - count,"Chances Left")
    for key, value in list1.items():
        print("Choose",key,"for",value)
    ur_choice = input()
    a = random.choice(list2)
    try:
        if list1[ur_choice]== a :
            print("You Choose", list1[ur_choice])
            print("Computer Choose ", a)
            count = count+1
            draw = draw+1
            print("You and Computer Both Wins")
        elif list1[ur_choice] == "Water" and a == "Snake"\
            or list1[ur_choice] == "Gun" and a == "Water"\
            or list1[ur_choice] == "Snake" and a == "Gun" :
            print("You Choose", list1[ur_choice])
            print("Computer Choose ", a)
            count = count+1
            c_score  = c_score + 1
            print("Computer Wins")
        elif list1[ur_choice] == "Water" and a == "Gun"\
            or list1[ur_choice] == "Gun" and a == "Snake"\
            or list1[ur_choice] == "Snake" and a == "Water" :
            print("You Choose", list1[ur_choice])
            print("Computer Choose ", a)
            count = count+1
            u_score = u_score + 1
            print("User Wins")
    except Exception as e :
        print("Invalid Choice, Try again...")
print("Computer Score =",c_score)
print("User Score =",u_score)
print(draw,"Rounds draw")
if c_score > u_score :
    print("Computer is Winner")
elif c_score < u_score:
    print("You are Winner")
else :
    print("Its a Tie,No One Wins")
