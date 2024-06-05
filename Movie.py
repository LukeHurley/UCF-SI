#Luke Hurley
#June 3rd 2024
#Movie Tickets
#ask for Kacie's # of friends
kp= int(input("How many people is Kacie bringing? "))
#ask for Mark's # of friends
mp = int(input("How many people is Mark bringing? "))
#Jack, Jill, Mark & Kacie
jjmk = 1+1+1+1
#all people
all= kp+mp+jjmk
#How much does popcorn cost?
popcorn= float(input("How much does popcorn cost per person? "))
#calculate the money they need to spend
noCorn = ((all)*8.50)/2
#calculate the money they need to spend with pop corn
withpopcorn = float(noCorn) + (all*popcorn)/2
#total without popcorn
print("Jack and Jill will each have to pay $", noCorn, " for all of the tickets.", sep="")
#total with popcorn
print("Jack and Jill will each have to pay $", withpopcorn, " if everyone wants popcorn.", sep="")
