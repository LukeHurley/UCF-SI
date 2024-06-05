#Luke Hurley
#June 3rd 2024
#Train Calculator
#distance
distance= float(input("What is the distance between the two trains? "))
#speed of 1st train
speed1 = float(input("What is the speed of the first train? "))
#speed of second train
speed2 = float(input("What is the speed of the second train? "))

#calculate how long it will take for them to meet
time = distance/((speed1+speed2)/60)
mph1 = speed1/60
mph2 = speed2/60
#print statement
print("The trains will meet in", time, "minutes.")
print("The first train will travel", mph1, "miles and the second train will travel", mph2," miles.")

      
