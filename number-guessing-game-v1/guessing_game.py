"""
Python Development Techdegree
Project 1 - The Number Guessing Game
--------------------------------
"""
import random
import time
# Import the random module.
# Create the start_game function.
# Write your code inside this function.

# Create start_game
high_scores = []


def start_game():
    # Print "Welcome To MAXIMUS Number Hunter"
    print("Welcome To MAXIMUS Number Hunter")
    # Prompt user for name
    name = input("What is your name? We will show your\n standings in the leaderboard:    ")
    # set correct_num to random int 1 - 10
    correct_num = random.randint(1, 10)
    # set guess_counter
    guess_counter = 1
    # set guess to 0
    guess = 0
# Begin Game Flow & Check Guess
    while guess != correct_num:
        guess = input("Please choose a number between 1 & 10:    ")
        if correct_num > int(guess):
            print("It's Higher")
            guess_counter += 1
        elif correct_num < int(guess):
            print("It's Lower")
            guess_counter += 1
# Set up and print tries and leaderboard
        else:
            print("You Got it")
            print(f"It only took you {guess_counter} tries")
            high_scores.append([name, guess_counter])
            print("####        Leaderboard        ####")
            high_scores.sort(key=lambda x: x[1])
            for name, score in high_scores:
                print(f"####      {name}         {score}      ####")
                time.sleep(.5)
            break
    play_again = input(f"Would you like to play again, {name}?   Y/N:    ")
    if play_again.lower() == "y":
        start_game()
    else:
        print("Thanks for playing!")
# print leaderboard

# prompt user to play again?


#   When the program starts, we want to:
#   ------------------------------------
#   1. Display an intro/welcome message to the player.
#   2. Store a random number as the answer/solution.
#   3. Continuously prompt the player for a guess.
#     a. If the guess is greater than the solution, display to the player "It's lower".
#     b. If the guess is less than the solution, display to the player "It's higher".

#   4. Once the guess is correct, stop looping, inform the user they "Got it"
#      and show how many attempts it took them to get the correct number.
#   5. Let the player know the game is ending, or something that indicates the game is over.

# ( You can add more features/enhancements if you'd like to.)


# Kick off the program by calling the start_game function.
start_game()
