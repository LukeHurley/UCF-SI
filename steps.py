#Luke Hurley
#June 3rd 2024
#Step Counter
#ask for goal
goal= int(input("What's your step goal for today?"))
#ask for current
now = int(input("How many steps have you taken so far?"))
#calculate the amount needed to reach goal
need = goal-now
print("Your Step Goal\n", goal, "Steps")
#current amount
print("How many steps you've taken so far\n", now, "Steps")
#how many you need
print("You need", need, "more steps to reach your goal")
