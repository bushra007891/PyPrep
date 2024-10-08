# Greet according to time program

'''Key Features of the Program:
1. Personalized Greeting: Greets the user based on their name.
2. Time-Based Logic: Determines greeting based on the current time.
3. Efficient Conditionals: Uses if-elif-else statements for decision-making.
4. Easy User Interaction: User only needs to enter their name.
5. Accurate Time-Based Greetings: Uses the system's current time to give appropriate responses.'''

# Importing the datetime module to get the current time
from datetime import datetime

# Taking user input for their name
name = input("Enter name: ")

# Getting the current time
time = datetime.now()

# Extracting the current hour in 24-hour format
hour = int(time.strftime("%H"))

# Checking the time and greeting accordingly
# Key Feature: Checks if the time is between 12 PM and 5 PM for afternoon greeting
if hour >= 12 and hour < 17:
    print(f"{name} Good Afternoon.")

# Key Feature: Checks if the time is between 5 PM and 12 AM for evening greeting
elif hour >= 17 and hour <= 19:
    print(f"{name} Good Evening.")

# Key Feature: If time is not in the above range, greet 'Good Night'
elif hour >= 19 and hour <= 24:
    print(f"{name} Good Night.")


    
