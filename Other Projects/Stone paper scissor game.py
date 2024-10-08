# Stone paper scissor game

'''Key Features:
1. Player can choose between stone (🪨), paper (📄), and scissors (✂️).
2. Random choice made by the computer.
3. Points are tracked for both the player and the computer.
4. Clear messages to indicate the outcome of each round.
5. Option to play multiple rounds can be added easily.'''

import random 

# Dictionary of choices
choices = {1: "🪨", 2: "📄", 3: "✂️"}
user_points = 0
computer_points = 0

def play_game():
    print("Welcome to the game of Stone Paper Scissors!")
    print("Press 1 for 🪨 (Stone)\nPress 2 for 📄 (Paper)\nPress 3 for ✂️ (Scissors)")
    
    # Get user input
    user_input = int(input("\nEnter your choice (1/2/3): "))
    
    # Computer randomly chooses
    computer_input = random.randint(1, 3)
    
    print(f"You chose: {choices[user_input]}")
    print(f"Computer chose: {choices[computer_input]}")

    # Determine the result
    if user_input == computer_input:
        return "tie"
    elif (user_input == 1 and computer_input == 3) or \
         (user_input == 2 and computer_input == 1) or \
         (user_input == 3 and computer_input == 2):
        return "you win"
    else:
        return "you lose"

# Play the game
while True:
    result = play_game()
    
    if result == "you win":
        user_points += 1
        print("🎉 You win this round!")
    elif result == "you lose":
        computer_points += 1
        print("😔 You lose this round.")
    else:
        print("🤝 It's a tie!")
    
    # Display current scores
    print(f"\nCurrent Scores: You - {user_points} | Computer - {computer_points}")

    # Ask if the user wants to play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break

print("Thanks for playing! Goodbye! 👋")
