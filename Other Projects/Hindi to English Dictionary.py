# Hindi to English Dictionary

'''Key Features:
- Provides English translations for common Hindi words.
- User-friendly interface for inputting Hindi words.
- Checks if the entered word exists in the dictionary.
- Displays an appropriate message if the word is not found.'''

# Dictionary containing Hindi words and their English meanings
dictionary = {
    "khana": "food",
    "paani": "water",
    "dost": "friend",
    "kitab": "book",
    "ghar": "home",
    "saat": "seven",
    "chand": "moon",
    "sooraj": "sun",
    "shukriya": "thank you",
    "aam": "mango"
}

# Prompt the user to enter a Hindi word
word = input("Enter the Hindi word which you want to find in the dictionary: ").lower()

# Check if the word exists in the dictionary
if word in dictionary:
    # If found, print the English translation
    print(f"The English version of '{word}' is {dictionary[word]}.")
else:
    # If not found, display an error message
    print(f"Sorry, the word '{word}' is not found in the dictionary.")
