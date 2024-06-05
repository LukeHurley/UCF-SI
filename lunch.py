#Luke Hurley
#June 5th 2024
#Lunch

#How much money did you get
money= float(input("How much money did your parents give you for lunch? "))
if money/5 >= 8.00:
    print("You will spend $8.00 for lunch on Monday.")
else:
    print("You will spend $",money/5," for lunch on Monday.", sep="")
