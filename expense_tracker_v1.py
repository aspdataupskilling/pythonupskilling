from sys import exit
from datetime import datetime
import traceback


def view_all_expenses():
    print("\n--- View All Expenses ---")
    # Example of sample data for expenses
    expenses = [
        {"Category": "Food     ", "Description": "Grocery         ", "Amount": 2000, "Date": "   02/12/2024"},
        {"Category": "Utilities", "Description": "Electric Bill   ", "Amount": 1500, "Date": "   15/11/2024"},
        {"Category": "Utilities", "Description": "Water Bill      ", "Amount": 300, "Date": "   15/11/2024"},
        {"Category": "Transpo  ", "Description": "Grab            ", "Amount": 750, "Date": "   20/10/2024"},
        {"Category": "Others   ", "Description": "Grand BINI-verse", "Amount": 12000, "Date": "   09/09/2024"},
        {"Category": "Food     ", "Description": "Steak           ", "Amount": 3500.75, "Date": "   05/11/2024"}
    ]

    print("Category\tDescription\t\tAmount\t   Date")
    print("-------------------------------------")
    for expense in expenses:
        print(f"{expense['Category']}\t{expense['Description']}\t{expense['Amount']}\t{expense['Date']}")
    print("\n")


def filter_by_month():
    while True:
        print("\n--- Filter Expenses by Month ---")
        month = input("Enter the month to filter by (01-12): ").strip()

        # Example of sample data for expenses
        expenses = [
            {"Category": "Food     ", "Description": "Grocery         ", "Amount": 2000, "Date": "   02/12/2024"},
            {"Category": "Utilities", "Description": "Electric Bill   ", "Amount": 1500, "Date": "   15/11/2024"},
            {"Category": "Utilities", "Description": "Water Bill      ", "Amount": 300, "Date": "   15/11/2024"},
            {"Category": "Transpo  ", "Description": "Grab            ", "Amount": 750, "Date": "   20/10/2024"},
            {"Category": "Others   ", "Description": "Grand BINI-verse", "Amount": 12000, "Date": "   09/09/2024"},
            {"Category": "Food     ", "Description": "Steak           ", "Amount": 3500.75, "Date": "   05/11/2024"}
        ]
        if "01" <= month <= "12":
            print("Category\tDescription\t\tAmount\t   Date")
            print("-------------------------------------")

            # Flag to check if any expenses match the month
            found = False

            for expense in expenses:
              # Clean the date string by removing leading/trailing spaces
              expense_date = expense['Date'].strip()

              # Convert the date string into a datetime object
              date_parts = expense_date.split('/')

              # Check if the month matches the desired month
              if date_parts[1] == month:
                print(f"{expense['Category']}\t{expense['Description']}\t{expense['Amount']}\t{expense['Date']}")
                found = True
            if not found:
                print(f"No records found for month {month}.")
            else:
                break

        else:
            print('Invalid input, please try again')


def filter_by_category():
    while True:
        print("\n--- Filter Expenses by Category ---")
        category = input("Enter the category (e.g., Food, Transpo): ").strip()

        # Example of sample data for expenses
        expenses = [
            {"Category": "Food     ", "Description": "Grocery         ", "Amount": 2000, "Date": "   02/12/2024"},
            {"Category": "Utilities", "Description": "Electric Bill   ", "Amount": 1500, "Date": "   15/11/2024"},
            {"Category": "Utilities", "Description": "Water Bill      ", "Amount": 300, "Date": "   15/11/2024"},
            {"Category": "Transpo  ", "Description": "Grab            ", "Amount": 750, "Date": "   20/10/2024"},
            {"Category": "Others   ", "Description": "Grand BINI-verse", "Amount": 12000, "Date": "   09/09/2024"},
            {"Category": "Food     ", "Description": "Steak           ", "Amount": 3500.75, "Date": "   05/11/2024"}
        ]

        print("Category\tDescription\t\tAmount\t   Date")
        print("-------------------------------------")
        found = False
        for expense in expenses:

            if expense["Category"].lower().strip() == category.lower():
                print(f"{expense['Category']}\t{expense['Description']}\t{expense['Amount']}\t{expense['Date']}")
                found = True
        if not found:
            print(f"No records found for category {category}.")
        else:
            break

def filter_by_amount():
    while True:
        print("\n--- Filter Expenses by Amount ---")

        try:
            amount = float(input("Enter the amount: "))

            # Example of sample data for expenses
            expenses = [
                {"Category": "Food     ", "Description": "Grocery         ", "Amount": 2000, "Date": "   02/12/2024"},
                {"Category": "Utilities", "Description": "Electric Bill   ", "Amount": 1500, "Date": "   15/11/2024"},
                {"Category": "Utilities", "Description": "Water Bill      ", "Amount": 300, "Date": "   15/11/2024"},
                {"Category": "Transpo  ", "Description": "Grab            ", "Amount": 750, "Date": "   20/10/2024"},
                {"Category": "Others   ", "Description": "Grand BINI-verse", "Amount": 12000, "Date": "   09/09/2024"},
                {"Category": "Food     ", "Description": "Steak           ", "Amount": 3500.75, "Date": "   05/11/2024"}
            ]

            print("Category\tDescription\t\tAmount\t   Date")
            print("-------------------------------------")
            found = False
            for expense in expenses:

                if expense["Amount"] == amount:
                    print(f"{expense['Category']}\t{expense['Description']}\t{expense['Amount']}\t{expense['Date']}")
                    found = True
            if not found:
                print(f"No records found for amount {amount}.")
            else:
                break
        except ValueError:
            print("Invalid amount. Please try again.")

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
        elif choice == '2':
            filter_by_month()
        elif choice == '3':
            filter_by_category()
        elif choice == '4':
            filter_by_amount()
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
