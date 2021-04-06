""" Number Guessing Game
----------------------------------------
"""
#Import the required libraries
import random

attempts_list = []


#Defining a function with name show_score
def show_score():
    #Trigger Function 'len' with parameters
    #Use conditional statement on parameters/check the options
    if len(attempts_list) <= 0:
        #Trigger Function 'print' with parameters
        print("There is currently no high score, it's yours for the taking!")
    else:
        #Trigger Function 'print' with parameters
        print("The current high score is {} attempts".format(
            min(attempts_list)))


#Defining a function with name start_game
def start_game():
    random_number = int(random.randint(1, 10))
    #Trigger Function 'print' with parameters
    print("Hello traveler! Welcome to the game of guesses!")
    player_name = input("What is your name? ")
    wanna_play = input(
        "Hi, {}, would you like to play the guessing game? (Enter Yes/No) ".
        format(player_name))

    attempts = 0
    #Trigger Function 'show_score' with parameters
    show_score()
    #Repeat action till ###iterator### completes
    while wanna_play.lower() == "yes":
        #To handle the exceptions raised during input/output
        try:
            guess = input("Pick a number between 1 and 10 ")
            #Trigger Function 'int' with parameters
            #Trigger Function 'int' with parameters
            #Use conditional statement on parameters/check the options
            if int(guess) < 1 or int(guess) > 10:
                #Trigger Function 'ValueError' with parameters
                raise ValueError(
                    "Please guess a number within the given range")
#Trigger Function 'int' with parameters
#Use conditional statement on parameters/check the options
            if int(guess) == random_number:
                #Trigger Function 'print' with parameters
                print("Nice! You got it!")
                attempts += 1
                attempts_list.append(attempts)
                #Trigger Function 'print' with parameters
                print("It took you {} attempts".format(attempts))
                play_again = input(
                    "Would you like to play again? (Enter Yes/No) ")
                attempts = 0
                #Trigger Function 'show_score' with parameters
                show_score()
                random_number = int(random.randint(1, 10))
                #Use conditional statement on parameters/check the options
                if play_again.lower() == "no":
                    #Trigger Function 'print' with parameters
                    print("That's cool, have a good one!")
                    break
#Trigger Function 'int' with parameters
#Use conditional statement on parameters/check the options
            elif int(guess) > random_number:
                #Trigger Function 'print' with parameters
                print("It's lower")
                attempts += 1
#Trigger Function 'int' with parameters
#Use conditional statement on parameters/check the options
            elif int(guess) < random_number:
                #Trigger Function 'print' with parameters
                print("It's higher")
                attempts += 1
        except ValueError as err:
            #Trigger Function 'print' with parameters
            print("Oh no!, that is not a valid value. Try again...")
            #Trigger Function 'print' with parameters
            print("({})".format(err))
    else:
        #Trigger Function 'print' with parameters
        print("That's cool, have a good one!")


#Use conditional statement on parameters/check the options
if __name__ == '__main__':
    #Trigger Function 'start_game' with parameters
    start_game()
