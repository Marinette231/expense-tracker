from datetime import date,datetime
import json

expenses = []

def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

def load_expenses():
    global expenses

    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)

    except FileNotFoundError:
        expenses = []
        print("No previous expenses found. Starting fresh.")

    except json.JSONDecodeError:
        expenses = []
        print("Warning: Expense file is corrupted. Starting fresh.")
        
def get_valid_amount():
    while True:
        try:
            amount = float(input("Enter amount: "))

            if amount <= 0:
                print("Amount must be greater than zero.")
                continue

            return amount

        except ValueError:
            print("Please enter a valid number.")
            
def add_expense():
    name = input("Enter expense name: ")
    amount = get_valid_amount()
    category = input("Enter expense category: ").strip().title()
    expense_date = str(date.today())

    expense = {
        "name": name,
        "amount": amount,
        "category": category,
        "date": expense_date
    }

    expenses.append(expense)
    save_expenses()

    print("Expense added successfully!")

def view_expenses():
    if not expenses:
        print("No expenses recorded.")
        return

    print("\n--- Expenses ---")
    total = 0

    for expense in expenses:
        print(
            f"{expense.get('name','Unknown')} | "
            f"{expense.get('category', 'Uncategorized')} | "
            f"{expense.get('date', 'Unknown')} | "
            f"₹{expense['amount']:.2f}")
        total += expense["amount"]

    print(f"Total: ₹{total:.2f}")

def filter_by_category():
    category = input("Enter category to filter: ").strip().title()

    found = False

    for expense in expenses:
        if expense.get("category", "").title() == category:
            print(
                f"{expense['name']} | "
                f"{expense.get('category', 'Uncategorized')} | "
                f"₹{expense['amount']:.2f}"
            )
            found = True

    if not found:
        print("No expenses found in this category.")

def monthly_summary():
    while True:
        month = input("Enter month (YYYY-MM): ")

        try:
            datetime.strptime(month, "%Y-%m")
            break

        except ValueError:
            print("Invalid month! Please use YYYY-MM (e.g. 2026-11).")

    total = 0
    found = False

    for expense in expenses:
        expense_date = expense.get("date", "")

        if expense_date.startswith(month) and len(expense_date) >= 7:
            total += expense["amount"]
            found = True

    if found:
        print(f"Total spending for {month}: ₹{total:.2f}")
    else:
        print("No expenses found for this month.")

def main():
    load_expenses()
    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Filter by Category")
        print("4. Monthly Expense Summary")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            filter_by_category()
        elif choice == "4":
            monthly_summary()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
