# This code is a password generator which is a useful tool that generates
# strong and random passwords for users.

import random
import string

def password_generator(length) :
    characters = string.ascii_letters + string.digits + string.punctuation
    password = '' .join(random.choice(characters) for i in range(length))
    return password

def password_length() :
    while True :
        try :
            length = int(input("Enter the desired length of the password: "))
            if length <= 0 :
                print("Length should be a positive integer.")
            else :
                return length
        except ValueError :
            print("Please enter a valid integer for the password length.")

def main() :
    print("      Random Password Generator")
    
    length = password_length()
    password = password_generator(length)

    print("Generating Password ........ \n")
    print("Generated Password is: " + str(password) + "\n")

if __name__ == "__main__" :
    main()
