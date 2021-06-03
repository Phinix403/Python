import random

startOrNot = int(input("Start - 1 \nNot - 0 \nEnter: "))

if startOrNot == 1:

    while True:
        no = random.randint(1, 6)

        print("\nDice - ", no)

        try:
            goOrNot = int(input("\nContinue - 1 \nNot - 0 \nEnter: "))
        except:
            print("\nEnter Correct Value\n")
            continue

        if goOrNot == 1:
            continue
        elif goOrNot == 0:
            print("Thanks for Playing")
            break
        else:
            print("\nEnter Correct Value\n")
            continue

elif startOrNot == 0:
    print("Thanks for Playing")

else:
    print("\nEnter Correct Value\n")