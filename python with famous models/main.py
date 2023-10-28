# Generating a random password of a specified length.
import random
import string

def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

password = generate_random_password(12)  # Generate a 12-character random password
print(f"Random password: {password}")
