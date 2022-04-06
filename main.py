# Isak Nordström
# Tetek20
# Lösenordssystem
# 2022-04-01

class Accounts:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        hide_pass = str("*")*len(self.password)
        return f"Username: {self.username}\nPassword: {hide_pass}"
    
    def return_name(self):
        return self.username

    def return_password(self):
        return self.password

def main():

    acc1 = Accounts(input("Input username: "), input("Input password: "))
    
    accounts = [acc1]
    for acc in accounts:
        print(acc)

if __name__ == "__main__":
    main() 
        