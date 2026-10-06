# ----------------------------------------------------------------------
# This is the file number_guesser.py
#
# The intent is to give you practice writing a complete, interactive
# Python program.
#
# Remove ALL of the existing comments in this file prior to submission.
# You can, and should, add your own comments, but please remove all the
# comments that are here now.
#
# Things to do:
#
# Generate a random number between 1 and 1000.
#
# Ask the user to guess the number. In your prompt, let the user know they
# can type 'bye' or 'exit' to quit the program.
#
# If their guess is not made up entirely of digits, print "Please enter a valid
# number" and ask them to guess again.
#
# If the guess is too high, print "Too high!" and continue asking.
#
# If the guess is too low, print "Too low!" and continue asking.
#
# If the guess is correct, print "Congratulations! You guessed the number!" along
# with the number of attempts it took to guess the number. Start over with a new
# random number. Make sure to zero out the number of attempts.
#
# Please note: There are likely to be a number of Python guessing games online,
# and most GenAI systems can probably write this for you. Don’t rely on them,
# as they rob you of a chance to practice your Python skills and they might not
# even be correct. Perhaps, worse, they might not follow the instructions
# exactly as given.
# ----------------------------------------------------------------------
import random

n=random.randint(1,1000)
playing=True
gc=1

print("I chose a random number between 1-1000. Guess the number. You can type 'bye' or 'exit' to quit. ")

while playing:
    guess = input("What is your guess?").lower().strip()
    if guess == "bye" or guess == "exit":
        gc=1
        print("Goodbye!")
        break 
    else:
        try:
            guess = int(guess)
        except ValueError:
              print("Please enter a valid number")
              continue 

    if guess == n:
        print("Congratulations! You guessed the number in " + str(gc) + " guesses!")
        playing=False
    elif guess > n:
        print("Too high!")
        gc=gc+1
    elif guess < n:
        print("Too low!")
        gc=gc+1


