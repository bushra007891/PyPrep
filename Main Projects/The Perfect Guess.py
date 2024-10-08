# The Perfect Guess

'''Key Features:
- The computer randomly selects a number between 1 and 10.
- The player tries to guess the number with feedback on whether their guess is too high or too low.
- The game continues until the player correctly guesses the number.'''

import random  # Import random module to generate random numbers

# Step 1: Initialize the user's guess to 0 and generate a random number for the computer
user_guess = 0
computer_guess = random.randint(1, 10)  # Computer randomly chooses a number between 1 and 10

# Step 2: Loop until the user guesses the correct number
while user_guess != computer_guess:
    # Step 3: Ask the user to input their guess
    user_guess = int(input("Enter a number between 1 to 10: "))

    # Step 4: Provide feedback based on the guess
    if user_guess < computer_guess:
        print("The number is too low. Try again.")
    elif user_guess > computer_guess:
        print("The number is too high. Try again.")
    else:
        # Correct guess
        print(f"Your guess '{user_guess}' is right and it matches the computer's guess '{computer_guess}'.")

# Final message after winning the game
print("Congratulations! You won the game.")
