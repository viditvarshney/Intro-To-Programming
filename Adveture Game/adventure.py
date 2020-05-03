'''

Project 2 Adventure Game Intro To Programming Nanodegree 



'''

import time
import random

# Print_with_Pause

def Print_with_Pause(print_this):
    
    print(print_this)
    time.sleep(2)


def introToGame(item, option):
    Print_with_Pause("You find yourself standing in an open field, filled with grass and yellow wildflowers.")
    Print_with_Pause("Rumor has it that a wicked fairie is somewhere around here, and has been terrifying the nearby village....")
    Print_with_Pause("In front of you is a house.")
    Print_with_Pause("To your right is a dark cave.")
    Print_with_Pause("In your hand you hold your trusty (but not very effective) dagger.")

def field(item, option):
    Print_with_Pause("")
    Print_with_Pause("Enter 1 to knock on the door of the house.")

    Print_with_Pause("Enter 2 to peer into the cave.")
    print("Please enter 1 or 2).")
    choice = int(input()) 
    # Choice Function

    lst  = [1,2]
    while True:  
     
        if(choice not in lst):
            print("Please enter 1 or 2).  ")
            choice = int(input())
        
    

        elif(choice == 1):
            house(item,option)
            break
        elif(choice == 2):
            cave(item,option)
    
            break

# if the user chooses 1 from field ( devil's house door)

def house(item, option):
    Print_with_Pause("You approach the door of the house.")
    Print_with_Pause("You are about to knock when the door opens and out steps a " + option + ".")
    Print_with_Pause("Eep! This is the " + option + "'s house!")
    Print_with_Pause("The " + option + " attacks you!")
    if "sward" not in item:
        Print_with_Pause("You feel a bit under-prepared for this, "
                    "what with only having a tiny dagger.")
    while True:
        choice2 = input("Would you like to (1) fight or (2) "
                        "run away?")
        #Fight with Devil 
        if choice2 == "1":
            if "sward" in item:   # check for the 'sward' 
                Print_with_Pause("As the " + option + " moves to attack, ""you unsheath your new sword.")
                Print_with_Pause("\nThe Sword of Ogoroth shines brightly in "
                            "your hand as you brace yourself for the "
                            "attack.")
                Print_with_Pause("\nBut the " + option + "takes one look at "
                            "your shiny new toy and runs away!")
                Print_with_Pause("\nYou have rid the town of the " + option +
                            ". You are victorious!\n")

            else:
                Print_with_Pause("\nYou do your best...")
                Print_with_Pause("but your dagger is no match for the "
                            + option + ".")
                Print_with_Pause("\nYou have been defeated!\n")
            play_again()
            break
        if choice2 == "2":
            Print_with_Pause("\nYou run back into the field. "
                        "\nLuckily, you don't seem to have been "
                        "followed.\n")
            field(item, option)
            break
                            
# If user chooses 2 from field (cave)

def cave(item,option):
    if "sward" in item:
        Print_with_Pause("\nYou peer cautiously into the cave.")
        Print_with_Pause("\nYou've been here before, and gotten all"
                    " the good stuff. It's just an empty cave"
                    " now.")
        Print_with_Pause("\nYou walk back to the field.\n")

    else:
        Print_with_Pause("\nYou peer cautiously into the cave.")
        Print_with_Pause("\nIt turns out to be only a very small cave.")
        Print_with_Pause("\nYour eye catches a glint of metal behind a "
                    "rock.")
        Print_with_Pause("\nYou have found the magical Sword of Ogoroth!")
        Print_with_Pause("\nYou discard your silly old dagger and take "
                    "the sword with you.")
        Print_with_Pause("\nYou walk back out to the field.\n")
        item.append("sward")
    field(item,option)

                            




    

# Play again Game

def play_again():
    again = input("Would you like to play again? (y/n)").lower()
    if again == "y":
        Print_with_Pause("\n\n\nExcellent! Restarting the game ...\n\n\n")
        play_game()
    elif again == "n":
        Print_with_Pause("\n\n\nThanks for playing! See you next time.\n\n\n")
    else:
        play_again()


def play_game():
    item = []
    option = random.choice(["wicked fairie", "pirate", "dragon", "troll",
                            "gorgon"])
    introToGame(item, option)
    field(item, option)

play_game()
