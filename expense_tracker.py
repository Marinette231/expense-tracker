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

    expense = {"name": name,"amount": amount}

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
        print(f"{expense['name']}: ₹{expense['amount']:.2f}")
        total += expense["amount"]

    print(f"Total: ₹{total:.2f}")


def main():
    load_expenses()
    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
