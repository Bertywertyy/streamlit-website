class BankAccount:
    def __init__(self, account_number):
        self.__account_number = account_number  # Private attribute
        self.__balance = 0.0                    # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount:.2f}. New balance: ${self.__balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: ${amount:.2f}. New balance: ${self.__balance:.2f}")
        elif amount > self.__balance:
            print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        return self.__balance  # Data hiding: return balance without allowing direct access

# Main function to test the BankAccount class with user interaction
def main():
    account_number = input("Enter your account balance: ")
    account = BankAccount(account_number)

    while True:
        print("\n--- Banking System ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == '3':
            print(f"Current balance: ${account.get_balance():.2f}")
        elif choice == '4':
            print("Exiting the banking system.")
            break
        else:
            print("Invalid choice. Please choose again.")

# Run the program
if __name__ == "__main__":
    main()
