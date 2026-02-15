from data import load_account_data, save_account_data

class BankAccount:
    """Represents a bank account with basic operations."""

    def __init__(self, account_number: str, initial_balance: float = 2000.0) -> None:
        if initial_balance < 0:
            raise ValueError("Initial cannot be negative.")
        
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        
        self.balance += amount
    
    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        
        self.balance -= amount

def get_valid_amount(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                raise ValueError
            return value
        except ValueError as e:
            print(f"Invalid input: {e}")

def main() -> None:
    account_number, balance = load_account_data()
    account = BankAccount(account_number, balance)

    menu = (
        "\n1. Check balance\n"
        "2. Deposit money\n"
        "3. Withdraw money\n"
        "4. Exit\n"
    )

    while True:
        print(menu)
        choice = input("Choose an option (1-4): ").strip()

        try:
            if choice == "1":
                print(f"Current balane: {account.balance}")
            
            elif choice == "2":
                amount = get_valid_amount("Enter deposit amount: ")
                account.deposit(amount)
                print(f"Deposite successful, New balance: {account.balance}")

            elif choice == "3":
                amount = get_valid_amount("Enter withdrawal amount: ")
                account.withdraw(amount)
                print(f"Withdrawal successful, New balance: {account.balance}")

            elif choice == "4":
                save_account_data(account.account_number, account.balance)
                print("Exiting the program.")
                break

            else:
                print("Invalid choice. Please select a valid option.")

        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()