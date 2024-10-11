# Random Password Generator

'''Key Features:
1. This program generates a random password of user-defined length.
2. The password includes a mix of alphabets (both upper and lower case), digits, and special characters.
3. It uses Python's `string` and `random` modules to create a secure and unpredictable password.'''

import string
import random

# Ask user for the desired length of the password
num = int(input("Enter the length of the password: "))

# Generate a password using random choices of alphabets, digits, and punctuation
alphabets = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=num))

# Display the generated password
print(alphabets)
