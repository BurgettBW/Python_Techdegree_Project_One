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
    if len(high_scores) == 0:
        print("")
        # print the high score to the counsel with correct grammar
    elif high_scores[0][1] == 1:
        print(f"{high_scores[0][0]} has the High Score with {high_scores[0][1]} try!")
    else:
        print(f"{high_scores[0][0]} has the High Score with {high_scores[0][1]} tries!")
    # Prompt user for name
    name = input("What is your name? We will show your\nstandings on the leaderboard:    ")

    # set correct_num to random int 1 - 10
    correct_num = random.randint(1, 10)
    # set guess_counter
    guess_counter = 1
    guess = 0
# Begin Game Flow & Check For Errors
    while guess != correct_num:
        guess = input("Please enter a number between 1 & 10:    ")
        try:
            int(guess)
            if int(guess) < 1 or int(guess) > 10:
                raise ValueError("Please choose a number between 1 and 10.")
        except TypeError:
            print("Please use only numerical characters... Try again")
            continue
        except ValueError:
            print(f"This is not a valid value, Please try again...    ")
            continue
        else:
            # Continue with checking the guess against to correct number
            if correct_num > int(guess):
                print("It's Higher")
                guess_counter += 1
            elif correct_num < int(guess):
                print("It's Lower")
                guess_counter += 1
# Set up and print tries and leaderboard
            else:
                print("You Got it")
                time.sleep(1.0)
                # Tell them how many tries it took them
                print(f"It only took you {guess_counter} tries")
                time.sleep(1.0)
                # Add name and score to leaderboard
                high_scores.append([name, guess_counter])
                print("####        Leaderboard        ####")
                # Sort the scores by tries and print them to the console
                high_scores.sort(key=lambda x: x[1])
                for name, score in high_scores:
                    print(f"####      {name}         {score}      ####")
                    time.sleep(.5)
                break
    # Ask them if they'd like to play again?
    play_again = input(f"Would you like to play again?    Enter Y or N:    ")
    if play_again.lower() == "y":
        start_game()
    else:
        print("Thanks for playing!")


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
