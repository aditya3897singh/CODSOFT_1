
import random
import string

# Taking password lenght
length = int(input("Enter the desired password length: "))

# Complexity check
use_numbers = input("Wanna include numbers? (yes/no): ").lower()
use_symbols = input("Wanna include symbols? (yes/no): ").lower()

# Ask number of symbols
num_symbols = 0

if use_symbols == "yes":
    num_symbols = int(input("How many symbols do you want to include? "))

# Select characters
characters = string.ascii_letters

if use_numbers == "yes":
    characters += string.digits

# Generate password
password = []

# Add the required number of symbols
if num_symbols > 0:
    password.extend(
        random.choices(string.punctuation, k=num_symbols)
    )

# Filling remaining length with other characters
remaining_length = length - num_symbols

if remaining_length < 0:
    print("Error: Number of symbols cannot exceed password length.")
else:
    password.extend(
        random.choices(characters, k=remaining_length)
    )

    # Shuffle password characters
    random.shuffle(password)

    # Display password
    password = ''.join(password)
    print("Generated Password:", password)