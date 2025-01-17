from sys import exit

import traceback


def view_all_expenses():
  print("\n--- View All Expenses ---")
  # Example of sample data for expenses
  expenses = [
    {"date": "2025-01-01", "category": "Food", "amount": 50.0},
    {"date": "2025-01-05", "category": "Transport", "amount": 20.0},
    {"date": "2025-01-10", "category": "Entertainment", "amount": 100.0}
  ]

  print("Date\t\tCategory\tAmount")
  print("-------------------------------------")
  for expense in expenses:
    print(f"{expense['date']}\t{expense['category']}\t{expense['amount']}")
  print("\n")


def expense_menu():
  while True:
    print("--------------------------------")
    print("View Expense")
    print("--------------------------------")
    print("1) View all expenses")
    print("2) Filtered by month")
    print("3) Filtered by category")
    print("4) Filtered by amount")
    print("x) Go Back")
    print("--------------------------------")

    choice = input("Choose an option > ").strip()

    if choice == '1':
      view_all_expenses()
    elif choice.lower() == 'x':
      break
    else:
      print("Invalid option. Please try again.\n")


def main_page():
  while True:
    print("--------------------------------")
    print("Personal Expense Tracker")
    print("--------------------------------")
    print("1) View Expenses")
    print("x) Exit")
    print("--------------------------------")

    choice = input("Choose an option > ").strip()

    if choice == '1':
      expense_menu()
    elif choice.lower() == 'x':
      print("Thank you for using Personal Expense Tracker!")
      break
    else:
      print("Invalid option. Please try again.\n")

