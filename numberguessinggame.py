#python number guessing game
# random module imprt cheyali because randint use cheysthm kabati
import random

lowest_number=1
highest_number=100
answer=random.randint(lowest_number,highest_number)
guesses = 0
is_running = True

print("---Number Guessing Game---")
print(f"select a number between: {lowest_number} and {highest_number}")

while is_running:
    
    guess=input("enter your guess:")

    if guess.isdigit():
        guess=int(guess)
        guesses += 1
        if guess < lowest_number or guess > highest_number:
            print(" the number is out of range ")
            print(f"select a number between:{lowest_number} and {highest_number}")
        elif guess > answer:
            print(" TO HIGH! try again ")
        elif guess < answer:
            print(" TO LOW! try again")
        else:
            print(f"CORRECT! The answer is : {answer}")
            print(f"number of guesses:{guesses}")
            is_running = False
    else: 
        print("INVALID")
        print(f"select a number between:{lowest_number} and {highest_number}")






