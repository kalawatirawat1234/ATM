class ATM:
    def __init__(self):

        # Initializes the ATM with default account details and an empty transaction history.
        
        self.balance = 0
        self.account_number = "12345678"
        self.pin = "1234"
        self.transaction_history = []

    def authenticate(self):
        """
        Authenticates the user by checking the entered account number and PIN.

        Returns:
            bool: True if authentication is successful, False otherwise.
        """
        print("Welcome to the ATM")
        entered_account_number = input("Enter account number: ")
        entered_pin = input("Enter PIN: ")

        if entered_account_number == self.account_number and entered_pin == self.pin:
            print("Authentication successful")
            return True
        else:
            print("Authentication failed")
            return False

    def display_menu(self):
        """
        Displays the main menu options for the ATM.
        """
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Change PIN")
        print("5. Transaction History")
        print("6. Exit")

    def check_balance(self):
        """
        Displays the current account balance.
        """
        print(f"Your current balance is: ${self.balance:.2f}")

    def deposit(self):
        """
        Allows the user to deposit money into their account.
        """
        try:
            amount = float(input("Enter amount to deposit: $"))
            if amount > 0:
                self.balance += amount
                self.transaction_history.append(f"Deposited: ${amount:.2f}")
                print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
            else:
                print("Deposit amount must be positive.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    def withdraw(self):
        """
        Allows the user to withdraw money from their account if sufficient funds are available.
        """
        try:
            amount = float(input("Enter amount to withdraw: $"))
            if amount > 0:
                if amount <= self.balance:
                    self.balance -= amount
                    self.transaction_history.append(f"Withdrew: ${amount:.2f}")
                    print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
                else:
                    print("Insufficient funds.")
            else:
                print("Withdrawal amount must be positive.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    def change_pin(self):
        """
        Allows the user to change their PIN after confirming the current PIN.
        """
        current_pin = input("Enter current PIN: ")
        if current_pin == self.pin:
            new_pin = input("Enter new PIN: ")
            self.pin = new_pin
            print("PIN changed successfully.")
        else:
            print("Current PIN is incorrect.")

    def display_transaction_history(self):
        """
        Displays the transaction history.
        """
        if self.transaction_history:
            print("\nTransaction History:")
            for transaction in self.transaction_history:
                print(transaction)
        else:
            print("No transactions found.")

    def run(self):
        """
        Runs the ATM machine simulation, handling user choices and interactions.
        """
        if not self.authenticate():
            return

        while True:
            self.display_menu()
            choice = input("Choose an option (1-6): ")
            if choice == "1":
                self.check_balance()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                self.change_pin()
            elif choice == "5":
                self.display_transaction_history()
            elif choice == "6":
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid option. Please choose again.")


if __name__ == "__main__":
    atm = ATM()
    atm.run()
