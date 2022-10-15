# 15. Write a program to input week number and print week day.

print("DAY [1] = MONDAY\nDAY [2] = TUESDAY\nDAY [3] = WEDNESDAY\nDAY [4] = THURSDAY"
      "\nDAY [5] = FRIDAY\nDAY [6] = SATURDAY\nDAY [7] = SUNDAY")
user_num = int(input("Enter a number between 1 to 7 to check it's day :"))

if user_num == 1:
      print("Day is Monday")
else:
      if user_num == 2:
            print("Day is Tuesday")
      else:
            if user_num == 3:
                  print("Day is Wednesday")
            else:
                  if user_num == 4:
                        print("Day is Thursday")
                  else:
                        if user_num == 5:
                              print("Day is Friday")
                        else:
                              if user_num == 6:
                                    print("Day is Saturday")
                              else:
                                    if user_num == 7:
                                          print("Day is Sunday")
                                    else:
                                          print("Please input correct number between 1 to 7.")
