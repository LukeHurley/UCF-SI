#Luke Hurley
#June 4th 2024
#Pictures

#Name
name = str(input("Enter the employee's name:\n"))
#Pay rate
rate= int(input("Enter the employee's pay rate ($/hr):\n"))
#overtime rate
OTRate= int(input("Enter the employee's overtime rate (eg. Enter 1.5 for time and a half)\n"))
#standard work week
weekNorm= int(input("Enter the employee's standard workweek (hrs)\n"))
#This work week
weekThis= int(input("Enter the number of hours the employee worked\n"))
#calculate how many hours worked over time
OT = (weekThis - weekNorm)
OTPay = OT*OTRate*rate
OTnone = weekThis - OT
norm = rate*OTnone
print(name, " gets paid $",OTPay + norm," this week.", sep="")

