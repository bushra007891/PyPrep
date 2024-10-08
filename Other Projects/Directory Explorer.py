# Directory Explorer
'''Key Features:
- Lists all files and directories in a specified folder.
- Uses Python's 'os' module to interact with the file system.
- Can be easily modified to explore any directory path.'''

import os  # Step 1: Import the os module to interact with the operating system

# Step 2: Specify the directory path (default is current directory '.')
directory_path = '.'  # '.' refers to the current directory, can be changed to any directory path

# Step 3: Get the list of contents (files and folders) in the directory
contents = os.listdir(directory_path)

# Step 4: Print the directory contents
print("Contents of the directory are:")
for item in contents:
    print(item)  # Loop through and print each item (file/folder) in the directory
