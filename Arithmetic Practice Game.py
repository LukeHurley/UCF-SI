#Luke Hurley
#June 5th 2024
#Arithmetic Practice Game
import random
#What is your name?
name1 = int(input("How many questions do you want? "))
top = int(input("What is the largest number to be used for the problems\nPlease enter 10, 12, 15, or 20."))
#RNG for problems
a = random.randint(2, top)
b = random.randint(2, top)
#question one
print("What is",a,"x", b,"?\n")
ans = int(input())
if ans == a*b:
    print("Correct!")
else:
    print("Incorrect",a,"x",b,"=",a*b)
#
#
#


