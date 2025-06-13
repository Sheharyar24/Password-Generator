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
    print("2. View password strength rules")
    print("3. Exit")
    
    user_choice = input("Select option: ")

    if user_choice == "1":
        password_length = int(input("Enter password length: "))
        password = Password(password_length)
        password = password.create_pass()
        print(f"\nGenerated Password:\n{password}\n")

    if user_choice == "3":
        break
    
