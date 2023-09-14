import random 
import string

def generate_password(length, use_lowercase, use_uppercase, use_numbers, use_special_chars):
    # Define character sets based on user-defined parameters
    lowercase_chars = string.ascii_lowercase if use_lowercase else ''
    uppercase_chars = string.ascii_uppercase if use_uppercase else ''
    digit_chars = string.digits if use_numbers else ''
    special_chars = '!@#$%^&*()_+-=[]{}|;:,.<>?/' if use_special_chars else ''

    # Combine character sets into a single set of allowed characters
    allowed_chars = lowercase_chars + uppercase_chars + digit_chars + special_chars

    # Check if at least one character set is selected
    if not allowed_chars:
        return "Please select at least one character set."

    # Generate the password
    password = ''.join(random.choice(allowed_chars) for _ in range(length))
    return password

def main():
    print("Password Generator")
    print("-------------------")

    try:
        # Get user-defined parameters
        length = int(input("Enter the desired password length: "))
        use_lowercase = input("Include lowercase letters? (yes/no): ").strip().lower() == 'yes'
        use_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
        use_numbers = input("Include numbers? (yes/no): ").strip().lower() == 'yes'
        use_special_chars = input("Include special characters? (yes/no): ").strip().lower() == 'yes'

        # Check for valid length
        if length <= 0:
            print("Password length must be a positive integer.")
            return

        # Generate and display the password
        password = generate_password(length, use_lowercase, use_uppercase, use_numbers, use_special_chars)
        print("\nGenerated Password:", password)

    except ValueError:
        print("Invalid input. Please enter a valid length (a positive integer).")

if __name__ == "__main__":
    main()
