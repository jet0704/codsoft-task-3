import random
import string

def get_password_length():
    while True:
        try:
            length = int(input("Enter the desired password length (at least 8): "))
            if length >= 8:
                return length
            else:
                print("Password length must be at least 8. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def generate_password(length):
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_characters) for _ in range(length))
    return password

def main():
    length = get_password_length()
    password = generate_password(length)
    print("Generated password:", password)

if __name__ == "__main__":
    main()