#Luke Hurley
#June 5th 2024
#Lemonade

LEMONS_PER_PITCHER = 12
SPOONS_PER_BAG = 1000
SPOONS_PER_PITCHER = 50
pitcher = 40

# of lemons
lemons= int(input("Enter the number of lemons you have: "))
# of bags
bags= int(input("Enter the number of bags of sugar you have: "))
#calc number of lemons and spoons of sugar
totalLemon = lemons//LEMONS_PER_PITCHER
totalSugar = (bags*SPOONS_PER_BAG)/SPOONS_PER_PITCHER
if totalLemon < totalSugar:
    pitcher = totalLemon
else:
    pitcher = totalSugar
print("You can make a maximum of",pitcher,"pitchers.")

