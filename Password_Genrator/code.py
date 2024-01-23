import string
import secrets

def password_generator(length, symbols, uppercase, lowercase, numbers):
    password = ""
    if symbols:
        password += string.punctuation
    if uppercase:
        password += string.ascii_uppercase
    if lowercase:
        password += string.ascii_lowercase
    if numbers:
        password += string.digits
    rang = len(password)
    output_password = ""
    for i in range(length):
        output_password += password[secrets.randbelow(rang)]
    return output_password

if __name__ == "__main__":
    print("Welcome to Password Generator")
    length = int(input("Enter the length of password: "))
    symbols = input("Do you want symbols in your password True or False: ")
    uppercase = input("Do you want uppercase in your password True or False: ")
    lowercase = input("Do you want lowercase in your password True or False: ")
    numbers = input("Do you want numbers in your password True or False: ")

    num = int(input("How many passwords do you want: "))
    for i in range(num):
        print("\n",password_generator(length, symbols, uppercase, lowercase, numbers))

    print("\nThank you for using Password Generator")






    