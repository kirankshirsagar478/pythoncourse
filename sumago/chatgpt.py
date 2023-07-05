class Account:
    def __init__(self, ac_no, pin, bal):
        self.ac_no = ac_no
        self.pin = pin
        self.bal = bal

    def deposit(self, amount):
        self.bal += amount
        print("Deposit successful.\n Current balance: ", self.bal)

    def withdraw(self, amount):
        if amount <= self.bal:
            self.bal -= amount
            print("Withdrawal successful.\n Current balance: ", self.bal)
        else:
            print("Insufficient balance: ", self.bal)

    def get_balance(self):
        print("Current balance: ", self.bal)


class ATM:
    def __init__(self):
        self.accounts = []

    def create_account(self):
        ac_no = input("Enter account number: ")
        while True:
            pin=int(input("Enter 4 Digit Pin:"))
            pin1=int(input("Confirm pin:"))
            if pin==pin1:
                print("Pin Created")
                break
            else:
                print("Wrong Pin")

        
        bal = float(input("Enter initial balance: "))
        account = Account(ac_no, pin, bal)
        self.accounts.append(account)
        print("Account created successfully!!.")

    def login(self):
        ac_no = input("Enter account number: ")
        pin = input("Enter PIN: ")

        for account in self.accounts:
            if account.ac_no == ac_no and account.pin == pin:
                print("Login successful.")
                self.perform_transactions(account)
                break
        else:
            print("Invalid account number or PIN.")

    def perform_transactions(self, account):
        while True:
            print("\n1. Deposit \n2. Withdraw \n3. Check balance \n4. Logout")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                amount = float(input("Enter the amount to deposit: "))
                account.deposit(amount)
            elif choice == 2:
                amount = float(input("Enter the amount to withdraw: "))
                account.withdraw(amount)
            elif choice == 3:
                account.get_balance()
            elif choice == 4:
                print("Logged out.")
                break
            else:
                print("Invalid choice!!! \nPlease try again.")

    def display_total_accounts(self):
        total_accounts = len(self.accounts)
        print("Total number of accounts:", total_accounts)

    def display_total_balance(self):
        total_bal = sum(account.balance for account in self.accounts)
        print("Total balance of all accounts: ", total_bal)


# Example usage
atm = ATM()

while True:
    print("\n1. Create account \n2. Login \n3. Total number of accounts \n4. Total balance \n5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        atm.create_account()
    elif choice == 2:
        atm.login()
    elif choice == 3:
        atm.display_total_accounts()
    elif choice == 4:
        atm.display_total_balance()
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
