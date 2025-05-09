import random
import string

def generate_password(length):
    """
    Generate a random password of given length with a mix of characters.
    """
    # Define character pools
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all characters
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters

    # Ensure password contains at least one character from each category
    password_chars = [
        random.choice(uppercase_letters),
        random.choice(lowercase_letters),
        random.choice(digits),
        random.choice(special_characters)
    ]

    # Fill the rest of the password length with random choices
    remaining_length = length - 4
    if remaining_length > 0:
        password_chars += random.choices(all_characters, k=remaining_length)

    # Shuffle the list to prevent predictable sequences
    random.shuffle(password_chars)

    # Join to form the password string
    password = ''.join(password_chars)
    return password

def main():
    print("Password Generator")
    while True:
        try:
            length = int(input("Enter the desired password length (minimum 4): "))
            if length < 4:
                print("Password length should be at least 4 to include all character types.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    password = generate_password(length)
    print(f"\nGenerated Password: {password}")

if __name__ == "__main__":
    main()
