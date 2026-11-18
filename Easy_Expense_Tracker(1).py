import json
import os
from datetime import date

FILE_NAME = "expenses.json"


def load_expenses():
    """Read saved expenses. Return an empty list if no file exists yet."""
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Saved data could not be read. Starting with an empty list.")
        return []


def save_expenses(expenses):
    """Save all expenses in a local JSON file."""
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    print("\n--- Add Expense ---")
    name = input("Enter expense name: ").strip()

    if not name:
        print("Expense name cannot be empty.")
        return

    try:
        amount = float(input("Enter amount (Rs.): "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    category = input("Enter category (Food/Travel/Study/Other): ").strip()
    if not category:
        category = "Other"

    expense = {
        "name": name,
        "amount": amount,
        "category": category,
        "date": str(date.today())
    }

    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully!")


def view_expenses(expenses):
    print("\n--- Expense History ---")

    if not expenses:
        print("No expenses found.")
        return

    print("-" * 65)
    print(f"{'No.':<5}{'Name':<20}{'Category':<15}{'Date':<13}{'Amount (Rs.)':>12}")
    print("-" * 65)

    for number, expense in enumerate(expenses, start=1):
        print(
            f"{number:<5}"
            f"{expense['name'][:19]:<20}"
            f"{expense['category'][:14]:<15}"
            f"{expense['date']:<13}"
            f"{expense['amount']:>12.2f}"
        )

    print("-" * 65)


def show_total(expenses):
    total = sum(expense["amount"] for expense in expenses)
    print(f"\nTotal expenses: Rs. {total:.2f}")
    print(f"Number of entries: {len(expenses)}")


def delete_expense(expenses):
    view_expenses(expenses)

    if not expenses:
        return

    try:
        number = int(input("Enter the expense number to delete: "))
        if number < 1 or number > len(expenses):
            print("Invalid expense number.")
            return
    except ValueError:
        print("Please enter a whole number.")
        return

    removed = expenses.pop(number - 1)
    save_expenses(expenses)
    print(f"'{removed['name']}' deleted successfully.")


def main():
    expenses = load_expenses()

    while True:
        print("\n========== EASY EXPENSE TRACKER ==========")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Show Total Expenses")
        print("4. Delete an Expense")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            show_total(expenses)
        elif choice == "4":
            delete_expense(expenses)
        elif choice == "5":
            print("Thank you for using Easy Expense Tracker!")
            break
        else:
            print("Invalid choice. Please select 1 to 5.")


if __name__ == "__main__":
    main()
