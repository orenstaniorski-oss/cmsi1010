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


