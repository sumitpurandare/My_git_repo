print("How many cats do you have?")
numcats=input()
try:
    if int(numcats)>=4:
        print("This is too many cats you have")
    else:
        print("You have ",numcats,"cats")
except ValueError:
    print("Please enter the integer and try again")