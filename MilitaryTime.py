#Luke Hurley
#June 4th 2024
#Militar Time

#How many seconds past midnight is it?
past= int(input("How many seconds past midnight is it? "))
#Ask for width of image
hours = 0
minutes = 0
seconds = 0
while (past > 0):
    if (past > 3600):
        past -= 3600
        hours += 1
        continue
    if (past > 60):
        past -= 60
        minutes += 1
        continue

    seconds = past
    past = 0


print("It is",hours, "hours,", minutes, "minutes, and", seconds," seconds past midnight.")


