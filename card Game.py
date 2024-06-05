#Luke Hurley
#June 5th 2024
#Card Game
import random
#What is your name?
name1 = input("What is your name? ")
name2 = input("What is the name of your first friend? ")
name3 = input("What is the name of your second friend? ")
#RNG for Die
roll_1 = random.randint(1, 4)
roll_2 = random.randint(1, 4)
roll_3 = random.randint(1, 4)

print(name1, " rolled a ",roll_1,".",sep="")
print(name2, " rolled a ",roll_2,".",sep="")
print(name3, " rolled a ",roll_3,".",sep="")


if roll_1 < roll_2 and roll_1 < roll_3:
    print(name1,"will go first!")
elif roll_2 < roll_1 and roll_2 < roll_3:
    print(name2,"will go first!")
elif roll_3 < roll_1 and roll_3 < roll_2:
    print(name3,"will go first!")
else:
   if name1 < name2 and name1 < name3:
    print(name1,"will go first!")
   elif name2 < name1 and name2 < name3:
    print(name2,"will go first!")
   else:
    print(name3,"will go first!")


