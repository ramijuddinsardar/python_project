# This program is an account management system that allows the user to view their balance, deposit money, and withdraw money.

class Account:
    def __init__(self, acc_no, bal):
        self.acc_no = acc_no
        self.bal = bal

    def debit(self):
        while True:
            try:
                amount = float(input("Enter the amount to withdraw: "))
                if amount <= 0:
                    print("Amount must be greater than 0. Please try again.")
                elif amount > self.bal:
                    print("Insufficient balance. Please try again.")
                else:
                    self.bal -= amount
                    print(f"You have withdrawn {amount} Rs. Current balance: {self.balance()} Rs.")
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def credit(self):
        while True:
            try:
                amount = float(input("Enter the amount to deposit: "))
                if amount <= 0:
                    print("Amount must be greater than 0. Please try again.")
                else:
                    self.bal += amount
                    print(f"You have deposited {amount} Rs. Current balance: {self.balance()} Rs.")
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def balance(self):
        return self.bal

    def balance_show(self):
        print(f"Your total balance is {self.balance()} Rs.")

acc1 = Account(8734153264, 5000)

while True:
    print("\n--- Account Menu ---")
    print("1. View Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        acc1.balance_show()
    elif choice == "2":
        acc1.credit()
    elif choice == "3":
        acc1.debit()
    elif choice == "4":
        print("Thank you for using the account system!")
        break
    else:
        print("Invalid choice. Please try again.")
