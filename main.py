import string
import random

class Password:
    def __init__(self, pass_len):
        self.pass_len = pass_len
        self.special = '!@#$%^&*()_+-?'

    def create_pass(self):
        t = random.choices(string.ascii_letters + string.digits + self.special, k=self.pass_len)
        return (''.join(t))

def save_password(passwords):
    with open("password.txt", "w") as file:
        file.write("Generated Passwords\n")
        
        for i in range(len(passwords)):
            file.write(f"{i+1}. {passwords[i]}\n")
        print("Passwords saved to file!\n")

## CLI interface
while True:
    print("=== Password Generator ===")
    print("1. Generate Password")
    print("2. Exit")
    print("==========================")

    user_choice = input("\nSelect option: ")

    if user_choice == "1":
        password_length = int(input("\nEnter password length (min 4, max 128): "))

        if password_length < 4 or password_length > 128:
            print("Please enter a length between 4 and 128!\n")
            continue
        
        num_of_pass = int(input("How many passwords would you like to generate: "))
        print("\nGenerated Password:\n")
        generated_pass = []

        for i in range(1,num_of_pass+1):
            password = Password(password_length)
            password = password.create_pass()
            generated_pass.append(password)
            print(f"{i}. {password}")
        print("")

        save_choice = input("Do you want to save these passwords to a file? (y/n): ").lower()
        if save_choice == 'y' or save_choice == 'yes':
            save_password(generated_pass)

    elif user_choice == "2":
        break

    else:
        print("Invalid option! (choose from 1 or 2)\n")