from random import randint

computer_lives = 4
player_lives = 4 
# available weapons => store this in an array
choices = ["Rock", "Paper", "Scissors"]
player = False

# make the computer pick one item at random
computer = choices[randint(0,2)]


# define a win or lose function instead of the procedural way
def winorlose(status):
    # handle win or lose based on the status we pass in
    print("Call the win or lose function") 
    print("*********************")
    print("You", status, "!" , "Would you like to play again?")
    choice = input("Y / N: ")

    if choice == "Y" or choice == "y":
        # reset the game
        # change global variables
        global player_lives
        global computer_lives
        global player
        global computer

        player_lives = 4
        computer_lives = 4
        player = False
        computer = choices[randint(0,2)]

    elif choice == "N" or choice == "n":
        print("You chose to quit")
        exit()    

while player == False:
    print("********************")
    print("Player Lives:", player_lives, "/4")
    print("AI Lives:", computer_lives, "/4")
    print("********************")
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
            player_lives -= 1
        else:
            print("You win", player, "smashes", computer)
            computer_lives -= 1 

    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cuts", player)
            player_lives -= 1
        else:
            print("You win", player, "covers", computer)
            computer_lives = 1

    elif player == "Scissors":
        if computer == "Rock":
            print("You lose", computer, "smashes", player)
            player_lives -= 1
        else:
            print("You win!", player, "cuts", computer)
            computer_lives -= 1 

    elif player == "Quit":
        exit()


    else:
        print("Not a valid option. Check again. and check your spelling\n")

    # handle win or loss
    if player_lives is 0:
        winorlose("lost")

    elif computer_lives is 0:
        winorlose("won")
    
    player = False
    computer = choices[randint(0, 2)]
