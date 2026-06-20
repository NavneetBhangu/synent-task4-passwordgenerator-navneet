import random
import string

print("===== ENHANCED PASSWORD GENERATOR =====")

try:
    # Password length
    password_length = int(input("Enter password length: "))

    if password_length <= 0:
        print("Please enter a valid positive number.")

    else:
        # User choices
        include_upper = input("Include uppercase letters? (y/n): ").lower()
        include_lower = input("Include lowercase letters? (y/n): ").lower()
        include_numbers = input("Include numbers? (y/n): ").lower()
        include_symbols = input("Include symbols? (y/n): ").lower()

        # Character pool
        characters = ""

        if include_upper == 'y':
            characters += string.ascii_uppercase

        if include_lower == 'y':
            characters += string.ascii_lowercase

        if include_numbers == 'y':
            characters += string.digits

        if include_symbols == 'y':
            characters += string.punctuation

        # Validation
        if characters == "":
            print("You must select at least one character type!")

        else:
            # Generate password
            password = ""

            for i in range(password_length):
                password += random.choice(characters)

            print("\nGenerated Password:", password)

            # Password Strength Checker
            if password_length < 6:
                print("Password Strength: Weak")
            elif password_length < 10:
                print("Password Strength: Medium")
            else:
                print("Password Strength: Strong")

except ValueError:
    print("Invalid input! Please enter a number.") 