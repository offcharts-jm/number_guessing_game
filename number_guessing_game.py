# Number Guessing Game by Jeremy Okeke

import random

def game():
    print("=== Number Guessing Game ===")
    secret = random.randint(1, 20)
    attempts = 0

    while True:
        guess = int(input("Guess a number between 1 and 20: "))
        attempts += 1

        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"Correct! You guessed it in {attempts} attempts.")
            break

game()
