# Snake water gun game

'''Key Features:
1. Added emojis to make the game fun 🐍 💧 🔫.
2. The player can choose between 'snake', 'water', and 'gun'.
3. The computer makes a random choice each time.
4. Keeps track of both player and computer scores.
5. Player can exit anytime by typing 'exit'.
6. Friendly messages guide the player during the game.
7. Shows the final scores after the player exits.'''

import random

# Function to decide the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie! 🤝"
    elif (user_choice == 'snake' and computer_choice == 'water') or \
         (user_choice == 'water' and computer_choice == 'gun') or \
         (user_choice == 'gun' and computer_choice == 'snake'):
        return "You win! 🎉"
    else:
        return "Computer wins! 😔"

# Variables to track scores
user_score = 0
computer_score = 0

# Loop to play the game multiple times
while True:
    print("\nLet's play Snake, Water, Gun!")
    print("Choose: 'snake 🐍', 'water 💧', or 'gun 🔫'.")
    print("Type 'exit' to quit the game. 😎")
    
    # Get user's choice
    user_choice = input("Your choice: ").lower()
    
    # Exit condition
    if user_choice == "exit":
        print(f"\nFinal scores - You: {user_score} ⭐ | Computer: {computer_score} 🖥️")
        print("Thanks for playing! See you next time! 😊👋")
        break
    
    # Validate input
    if user_choice not in ['snake', 'water', 'gun']:
        print("❌ Invalid input! Please choose either 'snake 🐍', 'water 💧', or 'gun 🔫'.")
        continue
    
    # Computer randomly chooses
    computer_choice = random.choice(['snake', 'water', 'gun'])
    
    # Show both choices
    print(f"\nYou chose: {user_choice} {('🐍' if user_choice == 'snake' else '💧' if user_choice == 'water' else '🔫')}")
    print(f"Computer chose: {computer_choice} {('🐍' if computer_choice == 'snake' else '💧' if computer_choice == 'water' else '🔫')}")
    
    # Determine and display the winner
    result = determine_winner(user_choice, computer_choice)
    print(f"\n🔔 Result: {result}")
    
    # Update scores based on the result
    if result == "You win! 🎉":
        user_score += 1
    elif result == "Computer wins! 😔":
        computer_score += 1
    
    # Display the current score
    print(f"\n🏆 Current scores -  You: {user_score}  | Computer: {computer_score}")

