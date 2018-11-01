from random import randint
print("***************")
computerlives = 2
playerlives = 2 
print("Welcome, you have ", playerlives, " lives.")
# available weapons => store this in an array
choices = ["Rock", "Paper", "Scissors"]
player = False

# make the computer pick one item at random
computer = choices[randint(0,2)]

#shows the computer choice in the terminal window
print("Computer chooses: ", computer)

while player == False:
    print("Choose Your Weapon\n")
    player = input("Rock,Paper or Scissors?\n")
    print("Player chooses:", player)

   #check for equality
    if (player == computer):
        print("Tie! Live to shoot another day")

    elif player == "Rock":
        if computer == "Paper":
        # computer won
            print("You lose!", computer, "covers", player)
            playerlives = playerlives-1
        else:
            print("You win", player, "smashes", computer)
            computerlives = computerlives-1

    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cuts", player)
            playerlives = playerlives -1
        else:
            print("You win", player, "covers", computer)
            computerlives = computerlives -1

    elif player == "Scissors":
        if computer == "Rock":
            print("You lose", computer, "smashes", player)
            playerlives = playerlives -1
        else:
            print("You win!", player, "cuts", computer)
            computerlives = computerlives -1

    elif player == "Quit":
        exit()


    else:
        print("Not a valid option. Check again. and check your spelling\n")

    print("Computer has", computerlives, "lives")
    if playerlives == 0:
        print("Player Loses")
    if computerlives == 0:
        print("Computer Loses")
        exit()
        print("Play again")
    
    player = False
    computer = choices[randint(0, 2)]
