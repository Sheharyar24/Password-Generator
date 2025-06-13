import string
import random

class Password:
    def __init__(self, pass_len):
        self.pass_len = pass_len
        self.special = '!@#$%^&*()_+-?'

    def create_pass(self):
        t = random.choices(string.ascii_letters + string.digits + self.special, k=self.pass_len)
        return (''.join(t))

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
        else:
            password = Password(password_length)
            password = password.create_pass()
            print(f"\nGenerated Password:\n{password}\n")

    if user_choice == "2":
        break
    
