# Text to Speech Generator

'''Key Features:
- Converts user input text into speech using the 'pyttsx3' library.
- Allows users to select male or female voice.
- Provides an option to download the speech as an MP3 file.'''

"""IMPORT MODULE"""
# Importing the pyttsx3 library for text-to-speech conversion
import pyttsx3
engine = pyttsx3.init()  # Initialize the engine for text to speech

"""VOICE"""
# Fetching available voices (male and female)
voices = engine.getProperty('voices')
# User chooses preferred voice type
voice_type = input("Which voice do you prefer? M/F: ")
if voice_type == 'M':
    engine.setProperty('voice', voices[0].id)  # Set to male voice
else:  
    engine.setProperty('voice', voices[1].id)  # Set to female voice

"""TEXT"""
# Taking text input from the user
text = input("Enter text: ")
# Convert the input text to speech
engine.say(text)
engine.runAndWait()  # Wait for the speech to complete

"""DOWNLOAD"""
# Option to save the speech to an MP3 file
download = input("Do you want to download this file? Y/N: ")
if download == "Y":
    file_name = input("Enter file name: ")  # User chooses file name
    engine.save_to_file(text, file_name + '.mp3')  # Save as an MP3 file
    engine.runAndWait()  # Wait for the save process to complete

"""CLOSING"""
# Ending message
print("Thank you for using Text to Speech Generator.")
