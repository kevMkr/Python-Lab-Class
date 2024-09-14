import random
randomnumber= random.randint(1,101)
while True:
    guessnumber= int(input())
    if (guessnumber > randomnumber):
        print("Lower")
    elif (guessnumber < randomnumber):
        print("Higher")
    elif (guessnumber == randomnumber):
        print("Nice")
        break 
