#Luke Hurley
#June 4th 2024
#Calories
import random
#Lowest num of Appetizer Cals
lowApp= int(input("What's the fewest number of calories your appetizer could have? "))
#Highest num of Appetizer Cals
hiApp= int(input("What's the most number of calories your appetizer could have? "))
#Lowest num of Entree Cals
lowEnt= int(input("What's the fewest number of calories your entree could have? "))
#Highest num of Entree Cals
hiEnt= int(input("What's the most number of calories your entree could have? "))

#RNG of Appetizer
rApp = random.randint(lowApp, hiApp)
#RNG of Entree
rEnt = random.randint(lowEnt, hiEnt)
#Cal in whole Meal
meal = rApp + rEnt
#lowest Cal Meal
lowMeal = lowApp + lowEnt
#highest Cal Meal
hiMeal = hiApp + hiEnt
print("Your appetizer has", rApp,"calories.")
print("Your entree has", rEnt,"calories.")
print("The least calories you could have gotten is", lowMeal)
print("The most calories you could have gotten is", hiMeal)
print("You acutally got", meal,"calories total.")




