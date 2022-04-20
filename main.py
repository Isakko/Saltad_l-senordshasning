# Isak Nordström
# Tetek20
# Lösenordssystem
# 2022-04-01

# Imports
import os
from os.path import exists

# Class where you create new accounts
class Accounts:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def return_name(self):
        return self.username

    def return_password(self):
        return self.password

    def __str__(self):
        hide_pass = str("*")*len(self.password)
        return f"Username: {self.username}\nPassword: {hide_pass}"

    def save_account(self):
        return f"{self.username}\n{self.password}"

# Function that clears console
def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

# Function that creates a new account
def create_account():
    clear_console()
    quantity = 1
    while True:

            choice = input("Vill du skapa ett konto? [Ja] eller [Nej]: ")
            clear_console()

            if choice.capitalize() == "Ja":
                
                acc = Accounts(input("Input username: "), input("Input password: "))

                clear_console()
                print(f"\n{acc}\n")
                
                while True:
                    
                    file_exists = exists("account"+str(quantity)+".txt")

                    if file_exists:
                        quantity+=1

                    else:
                        with open("account"+str(quantity)+".txt", "a", encoding="utf8") as all_accounts:
                                all_accounts.write(acc.save_account())
                        break
                    
            
                        
            elif choice.capitalize() == "Nej":
                print("Återvänder till huvudmenyn...")
                break

# Main
def main():

    clear_console()

    while True:

        clear_console()

        print("""\nVälkommen till kontosidan!\n
    1. Skapa nytt konto
    2. Logga in på konto
    3. Avsluta programmet
                """)

        main_choice = input("Skriv in siffra för ditt val: ")
        if main_choice == str(1):
            create_account()
        elif main_choice == str(2):
            continue
        elif main_choice == str(3):
            clear_console()
            print("Programmet avslutas...")
            break 

if __name__ == "__main__":
    main() 
        