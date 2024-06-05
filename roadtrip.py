#Luke Hurley
#June 3rd 2024
#Gas Calculator
#Price of Gas per Gallon
price= float(input("What is the price of gasoline per gallon? "))
#Amount of gas in car
current = float(input("How many gallons of gas are currently in your car? "))
#How many MPG does it get
mpg = float(input("How many miles per gallon does your car get? "))
#How long is your road trip?
length = float(input("What is the length of your road trip? "))
#calculate the price of gas
money = (((length -(mpg*current))/mpg)*price)
#print statement
print("You will have to spend" ,money, "dollars on gas to complete your road trip.")
