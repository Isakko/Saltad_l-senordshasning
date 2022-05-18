# Isak Nordström
# Tetek20
# Lösenordssystem
# 2022-04-01

# Imports
import os
from os.path import exists
from time import localtime, strftime

class Accounts:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def return_name(self):
        return self.username

    def return_password(self):
        return self.password

    def __str__(self):
        """String of attributes

        Returns:
            str, str: Username: 'Username', Password: 'Password'
        """

        return f"Username: {self.username}\nPassword: {self.password}"

    def save_account(self):
        """Use to save to file

        Returns:
            str, str: Username, Password
        """

        return f"{self.username}\n{self.password}"

def clear_console():

    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def create_account():
    """Creates account with username and password, stores it in a separate .txt file
    """
    clear_console()
    quantity = 1
    while True:

            acc = Accounts(input("Input username: "), input("Input password (Atleast one capital letter, one number and 6 letters long!): "))
            
            if acc.password.islower() == False and len(acc.password) >= 6 and has_numbers(acc) == True:
                
                print(f"\n{acc}\n")
                
                while True:
                    
                    file_exists = exists("account"+str(quantity)+".txt")

                    if file_exists:
                        quantity+=1

                    else:
                        acc.password = crypted_pass(acc)
                        with open("account"+str(quantity)+".txt", "a", encoding="utf8") as all_accounts:
                                all_accounts.write(acc.save_account())
                        new_user_log()

                        break
                            
                print("Returning to main menu...")
                break

            else:
                print("Password does not meet the requirements...")

def has_numbers(acc:Accounts):
    return any(char.isdigit() for char in acc.password)

def new_user_log():
    with open("log.txt", "a", encoding="utf8") as the_log:
        the_log.write(str(strftime("New user created! (%a, %d %b %Y %H:%M:%S)", localtime())))
        the_log.write(str("\n"))

def pass_change_log():
    with open("log.txt", "a", encoding="utf8") as the_log:
        the_log.write(str(strftime("Account password changes! (%a, %d %b %Y %H:%M:%S)", localtime())))
        the_log.write(str("\n"))

def login_acc_log():
    with open("log.txt", "a", encoding="utf8") as the_log:
        the_log.write(str(strftime("User login attempt or success! (%a, %d %b %Y %H:%M:%S)", localtime())))
        the_log.write(str("\n"))

def login_account():
    """Logins on existing account looping through .txt files
    """
    clear_console()

    quantity = 1
    while True:

        print("Login below:\n")
        acc = Accounts(input("Input username: "), input("Input password: "))
        acc.password = crypted_pass(acc)
        print(acc.password)
        while True:
                
            file_exists = exists("account"+str(quantity)+".txt")
            logged_in = False
            if file_exists:
                with open("account"+str(quantity)+".txt", "r", encoding="utf8") as searchfile:
                    lines = searchfile.readlines()
                    if acc.username == lines[0].rstrip("\n") and acc.password == lines[1]: 
                        clear_console()
                        print("\nLogin successful!")
                        login_acc_log()
                        logged_in = True
                        change_pass(acc)
                    else:
                        quantity+=1
                if logged_in: break

            else:
                print("\nUser authorization failure....")
                login_acc_log()
                break
        break

def crypted_pass(acc:Accounts):
    """Takes in password and encrypts it.

    Args:
        acc (Accounts): password

    Returns:
        str: crypted passwordd
    """

    letters = "ABCDEFGHIJKLMNOPQRSTUVXYZÅÄÖ"
    shifted_numbers = "=!'#¤%&/()"
    
    encrypted = ""

    for i in range(len(acc.password)):
        
        if acc.password[i].isupper():
            if acc.password[i] == str("Ö"):
                
                encrypted += acc.password[i].replace(acc.password[i], letters[0].lower())
            else:
                where = letters.index(acc.password[i])
                
                encrypted += acc.password[i].replace(acc.password[i], letters[where+1].lower())

        elif acc.password[i].islower():
            if acc.password[i] == str("ö"):
                
                encrypted += acc.password[i].replace(acc.password[i], letters[0].upper())
            else:
                where = letters.index(acc.password[i].upper())
                
                encrypted += acc.password[i].replace(acc.password[i], letters[where+1].upper())

        elif has_numbers(acc) == True:
            x = acc.password[i]
            if x == 9:
                encrypted+= acc.password[i].replace(acc.password[i], shifted_numbers[int(acc.password[x-1])])
            else:
                encrypted+= acc.password[i].replace(acc.password[i], shifted_numbers[int(acc.password[i])])

        else:
            encrypted += acc.password[i] 
    
    acc.password = encrypted
    return acc.password

def decrypt_pass(acc:Accounts):
    """Takes in crypted password and decrypts it.

    Args:
        acc (Accounts): crypted password

    Returns:
        str: decrypted password
    """
    letters = "ABCDEFGHIJKLMNOPQRSTUVXYZÅÄÖ"
    shifted_numbers = "=!'#¤%&/()"
    numbers = "0123456789"
    
    encrypted = ""
    
    for i in range(len(acc.password)):

        if acc.password[i].isupper():
            where = letters.index(acc.password[i])
            
            encrypted += acc.password[i].replace(acc.password[i], letters[where-1].lower())

        elif acc.password[i].islower():
            where = letters.index(acc.password[i].upper())

            encrypted += acc.password[i].replace(acc.password[i], letters[where-1].upper())
         
        elif acc.password[i] in shifted_numbers: 
            x = shifted_numbers.index(acc.password[i])
            
            encrypted+= acc.password[i].replace(acc.password[i], numbers[x])
         
        else:
            encrypted += acc.password[i] 
    
    acc.password = encrypted
    
    return acc.password

def has_numbers_new(new_pass):
    return any(char.isdigit() for char in new_pass)

def change_pass(acc:Accounts):
    """Used in login function, takes in old pass and new pass, changes password to specific account to new pass.

    Args:
        acc (Accounts): Username, password

    Returns:
        str: password
    """
    quantity = 1

    choice = input("\nInput 'passwd' to change password or 'meny' to return to the menu: ")
        
    while True:

        if choice == "passwd":
            clear_console()
            print("Welcome to the password changer!\n")

            old_pass = input("Input old password: ")
            decrypt_pass(acc)
            if old_pass == acc.password:
                crypted_pass(acc)
                new_pass = input("Input password (Atleast one capital letter, one number and 6 letters long!): ")
                
                if not new_pass.islower() and len(new_pass) >= 6 and has_numbers_new(new_pass):
                   
                    while True:
                    
                        file_exists = exists("account"+str(quantity)+".txt")
                        print("2")
                        if file_exists:
                            with open("account"+str(quantity)+".txt", "r", encoding="utf8") as searchfile:
                                lines = searchfile.readlines()
                                if acc.password == lines[1]: 
                                    with open("account"+str(quantity)+".txt", "w", encoding="utf8") as searchfile:
                                        print("4")
                                        acc.password = new_pass
                                        crypted_pass(acc)
                                        
                                        searchfile.write(acc.save_account())
                                        clear_console()
                                        print("\nPassword changed!")
                                        pass_change_log()
                                        break
                                
                                else:
                                  quantity+=1

                        else:
                            quantity+=1
                        
                else:
                    print("Password does not meet the requirements...")
                break

            else:
                print("User authorization failure...")
                break

        elif choice == "meny":
            clear_console()
            break

        else:
            print("\nError")
            break

# Main
def main():

    clear_console()

    while True:

        print("""\nWelcome to the menu!\n
    1. Create new account
    2. Login on existing account
    3. Quit program
                """)

        main_choice = input("Input number for your choice: ")
        if main_choice == str(1):
            create_account()
        elif main_choice == str(2):
            login_account()
        elif main_choice == str(3):
            clear_console()
            print("\nQuitting program...\n")
            break 

if __name__ == "__main__":
    main() 
        