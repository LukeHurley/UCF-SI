#Luke Hurley
#June 5th 2024
#Spending Spree

#constants
SHOE = int(80)
GAME = int(50)
SHIRT = int(15)
MAKEUP = int(25)
#Amound Saved
saved = int(input("How many dollars have you saved?\n$"))
if saved > SHIRT:
#Buy Shoe
    if saved - SHOE > 0:
        saved -= SHOE
        print("Great, you can buy a pair of your favorite shoes!\nYour new total is", saved)
    else:
        print("Unfortunately, your favorite shoes won't fit in your budget.")
#Buy Game
    if saved - GAME > 0:
        saved -= GAME
        print("Great, you can buy that new Nintendo game you've been wanting!\nYour new total is", saved)
    else:
        print("Unfortunately, that new game won't fit in your budget.")
#Buy Shirt
    if saved - SHIRT > 0:
        saved -= SHIRT
        print("Great, you can buy that t-shirt you've been wanting!\nYour new total is", saved)
    else:
        print("Unfortunately, the t-shirt you wanted doesn't fit in your budget.")
#Buy Makeup
    if saved - MAKEUP > 0:
        saved -= MAKEUP
        print("Great, you can buy that make up you've been eyeing!")
    else:
        print("Unfortunately, that new makeup you've been eyeing won't fit in your budget.")
else:
    print("Sorry, you can not buy any of your items.")

print("After your shopping spree, you have",saved,"dollars left.")



