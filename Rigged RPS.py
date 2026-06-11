import random


choice = int(input("Select an option \n1 = Rock \n2 = Paper \n3 = Scissors \n"))

if choice not in (1, 2, 3):
    print("Invalid selection")
else:

    check = random.randint(1, 100)

    computer = random.randint(1, 3)

    if check <= 70:
        print("The game was rigged from the start")
        if choice == 1:
            computer = 2
        elif choice == 2:
            computer = 3
        elif choice == 3:
            computer = 1

    if choice == computer:
        print("It's a tie")

    elif choice == 1 and computer == 2:
        print("You lose")
    elif choice == 1 and computer == 3:
        print("You win")

    elif choice == 2 and computer == 1:
        print("You win")
    elif choice == 2 and computer == 3:
        print("You lose")

    elif choice == 3 and computer == 1:
        print("You lose")
    elif choice == 3 and computer == 2:
        print("You win")
