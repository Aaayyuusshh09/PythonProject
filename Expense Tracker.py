"""
Expense Tracker
Covers: input, variables, data types, lists, dicts, functions, loops,
if-else, nesting, global vars/constants, docstrings, file handling
"""

import datetime

# ---- Global Constant ----
EXPENSE_FILE = "expenses.txt"

# ---- Expenses List ----
expenses = []  # each expense will be a dictionary


# ---- Functions ----

def add_expense():
    """Add a new expense entry"""
    category = input("Enter category (Food, Travel, Shopping, etc.): ")
    try:
        amount = float(input("Enter amount spent: ₹"))
    except ValueError:
        print("⚠️ Invalid input. Amount must be a number.")
        return

    date = datetime.date.today().strftime("%Y-%m-%d")

    expense = {"date": date, "category": category, "amount": amount}
    expenses.append(expense)

    print(f"✅ Expense added: {category} - ₹{amount} on {date}")


def show_expenses():
    """Display all expenses"""
    if not expenses:
        print("⚠️ No expenses recorded yet.")
        return

    print("\n--- Expense List ---")
    for e in expenses:
        print(f"{e['date']} | {e['category']} | ₹{e['amount']}")


def total_expense():
    """Show total expenses"""
    total = sum(e["amount"] for e in expenses)
    print(f"\n💰 Total Expenses: ₹{total}")


def category_summary():
    """Show expenses by category"""
    if not expenses:
        print("⚠️ No expenses recorded yet.")
        return

    summary = {}
    for e in expenses:
        summary[e["category"]] = summary.get(e["category"], 0) + e["amount"]

    print("\n📊 Expense Summary by Category:")
    for cat, amt in summary.items():
        print(f"{cat}: ₹{amt}")


def save_expenses():
    """Save all expenses to a file"""
    with open(EXPENSE_FILE, "w") as f:
        for e in expenses:
            f.write(f"{e['date']},{e['category']},{e['amount']}\n")
    print(f"💾 Expenses saved to {EXPENSE_FILE}")


def load_expenses():
    """Load expenses from file if exists"""
    try:
        with open(EXPENSE_FILE, "r") as f:
            for line in f:
                date, category, amount = line.strip().split(",")
                expenses.append({"date": date, "category": category, "amount": float(amount)})
        print("📂 Previous expenses loaded successfully.")
    except FileNotFoundError:
        print("⚠️ No previous expenses found.")


def expense_menu():
    """Main menu for expense tracker"""
    load_expenses()  # load previous data on start

    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. Show All Expenses")
        print("3. Show Total Expense")
        print("4. Category-wise Summary")
        print("5. Save & Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            category_summary()
        elif choice == "5":
            save_expenses()
            print("👋 Exiting. Stay mindful of your spending!")
            break
        else:
            print("❌ Invalid choice, try again.")


# ---- Run Program ----
expense_menu()
