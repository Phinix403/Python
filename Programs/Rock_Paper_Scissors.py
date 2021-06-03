# Rock Paper Scissor
import random

choice = int(input("How Much Choice you needs: "))

computer_points = 0
player_points = 0

turns = choice

while True:
    try:
        userInp = int(input("Rock -> 1 \nPaper -> 2 \nScissors -> 3 \nEnter:"))
    except:
        print("Enter Correct Value")
        break

    computerInp = random.randint(1, 3)

    if userInp ==  computerInp:
        print("\nDraw!\n")

    elif userInp == 1 and computerInp == 2:
        print("\nComputer --> 2 \nPlayer --> 1 \n *** Computer Won 1 Point ***\n")
        computer_points += 1

    elif userInp == 2 and computerInp == 1:
        print("\nComputer --> 1 \nPlayer --> 2 \n *** Player Won 1 Point ***\n")
        player_points += 1

    elif userInp == 2 and computerInp == 3:
        print("\nComputer --> 3 \nPlayer --> 2 \n *** Computer Won 1 Point ***\n")
        computer_points += 1

    elif userInp == 3 and computerInp == 2:
        print("\nComputer --> 2 \nPlayer --> 3 \n *** Player Won 1 Point ***\n")
        player_points += 1

    elif userInp == 3 and computerInp == 1:
        print("\nComputer --> 1 \nPlayer --> 3 \n *** Computer Won 1 Point ***\n")
        computer_points += 1

    elif userInp == 1 and computerInp == 3:
        print("\nComputer --> 3 \nPlayer --> 1 \n *** Player Won 1 Point ***\n")
        player_points += 1

    else:
        print("\nSomething went Wrong\n")
        continue

    turns -= 1
    print(turns, "Turns Left\n")

    if turns == 0:
        break

print(f"Results: \n Computer Points = {computer_points}\n Player Points = {player_points}")

if player_points > computer_points:
    print("\nYou Won!!")

elif player_points < computer_points:
    print("\nYou Loss!")
    
else:
    print("\n Draw!!")