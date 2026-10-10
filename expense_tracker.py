
import csv
import os
from collections import defaultdict

FILE_NAME = "expenses.csv"

def add_expense():
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category: ")
    description = input("Enter description: ")
    amount = float(input("Enter amount: "))

    file_exists = os.path.exists(FILE_NAME)

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists or os.path.getsize(FILE_NAME) == 0:
            writer.writerow(["Date", "Category", "Description", "Amount"])

        writer.writerow([date, category, description, amount])

    print("Expense added successfully!")

def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("No expenses found.")
        return

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            print(" | ".join(row))

def filter_expenses():
    category = input("Enter category to filter: ").lower()

    if not os.path.exists(FILE_NAME):
        print("No expenses found.")
        return

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)
        found = False

        for row in reader:
            if row["Category"].lower() == category:
                print(row)
                found = True

        if not found:
            print("No expenses in this category.")

def category_summary():
    totals = defaultdict(float)

    if not os.path.exists(FILE_NAME):
        print("No expenses found.")
        return

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            totals[row["Category"]] += float(row["Amount"])

    print("Category-wise Summary:")
    for category, total in totals.items():
        print(f"{category}: {total:.2f}")

while True:
    print("\n--- Personal Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Filter by Category")
    print("4. Category Summary")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        filter_expenses()
    elif choice == "4":
        category_summary()
    elif choice == "5":
        print("Thank you!")
        break
    else:
        print("Invalid choice. Try again.")
  
