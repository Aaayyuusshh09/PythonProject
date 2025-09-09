"""
Bank Account Simulation
Covers: input, variables, data types, if-else, loops, functions, dicts,
lists, nesting, random, global vars/constants, scope, docstrings
"""

import random  # Module use (for random transaction ID)

# ---- Global Constant ----
BANK_NAME = "Python Bank"

# ---- Global Variable ----
accounts = {}  # Store account details in dictionary


# ---- Functions ----

def create_account():
    """Create a new bank account with random account number"""
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    if age < 18:
        print("❌ You must be 18 or older to open an account.")
        return

    acc_num = random.randint(1000, 9999)  # random account number
    accounts[acc_num] = {"name": name, "balance": 0}
    print(f"✅ Account created! Account No: {acc_num}")


def deposit():
    """Deposit money into an account"""
    acc_num = int(input("Enter account number: "))
    if acc_num in accounts:
        amount = float(input("Enter amount to deposit: "))
        accounts[acc_num]["balance"] += amount
        print(f"💰 {amount} deposited. New Balance: {accounts[acc_num]['balance']}")
    else:
        print("❌ Invalid account number.")


def withdraw():
    """Withdraw money if balance is sufficient"""
    acc_num = int(input("Enter account number: "))
    if acc_num in accounts:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= accounts[acc_num]["balance"]:
            accounts[acc_num]["balance"] -= amount
            print(f"✅ {amount} withdrawn. Remaining Balance: {accounts[acc_num]['balance']}")
        else:
            print("❌ Insufficient funds.")
    else:
        print("❌ Invalid account number.")


def check_balance():
    """Check balance of an account"""
    acc_num = int(input("Enter account number: "))
    if acc_num in accounts:
        print(f"📊 Balance for {accounts[acc_num]['name']} : {accounts[acc_num]['balance']}")
    else:
        print("❌ Invalid account number.")


def bank_menu():
    """Main menu for the bank simulation"""
    while True:
        print(f"\n--- Welcome to {BANK_NAME} ---")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            check_balance()
        elif choice == "5":
            print("👋 Thank you for banking with us!")
            break
        else:
            print("❌ Invalid choice, try again.")


# ---- Run Program ----
bank_menu()
