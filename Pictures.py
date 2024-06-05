#Luke Hurley
#June 4th 2024
#Pictures

#ask for the amount of gigabytes in thumb drive
gigs= int(input("How many gigabytes can your thumb drive store? "))
#Ask for width of image
wide= int(input("What is the width of each picture in pixels? "))
#Ask for height of image
tall= int(input("and height? "))
#amound of bytes in a gig
bytes = 1073741824
#convert gb to bytes
totalbytes = bytes*gigs
#find the size
size = tall*wide*3
#find the amound of pictures that it can store
store = totalbytes//size

print("You can store", store," pictures on your thumb drive.")

