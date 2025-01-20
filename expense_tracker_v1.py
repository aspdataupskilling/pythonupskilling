from sys import exit
import traceback

expenses = [
    {"Category": "Food     ", "Description": "Grocery         ", "Amount": 2000, "Date": "   02/12/2024"},
    {"Category": "Utilities", "Description": "Electric Bill   ", "Amount": 1500, "Date": "   15/11/2024"},
    {"Category": "Utilities", "Description": "Water Bill      ", "Amount": 300, "Date": "   15/11/2024"},
    {"Category": "Transpo  ", "Description": "Grab            ", "Amount": 750, "Date": "   20/10/2024"},
    {"Category": "Others   ", "Description": "Grand BINI-verse", "Amount": 12000, "Date": "   09/09/2024"},
    {"Category": "Food     ", "Description": "Steak           ", "Amount": 3500.75, "Date": "   05/11/2024"}
]

def view_all_expenses():
    print("\n--- View All Expenses ---")

    print("Category\tDescription\t\tAmount\t   Date")
    print("-------------------------------------")
    for expense in expenses:
        print(f"{expense['Category']}\t{expense['Description']}\t{expense['Amount']}\t{expense['Date']}")
    print("\n")


def filter_by_month():
    while True:
        print("\n--- Filter Expenses by Month ---")
        month = input("Enter the month to filter by (01-12): [Enter x to go back] > ").strip()

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
        elif 'x' == month.lower():
            break
        else:
            print('Invalid input, please try again')


def filter_by_category():
    while True:
        print("\n--- Filter Expenses by Category ---")
        print("-------------------------------------")
        print("1) Food")
        print("2) Utilities")
        print("3) Transpo")
        print("4) Others")
        print("x) Go Back")
        print("-------------------------------------")
        category = input("Enter the category (e.g., Food, Transpo): [Enter x to go back] > ").strip()

        found = False
        if 'x' == category.lower():
            break
        else:
            print("Category\tDescription\t\tAmount\t   Date")
            print("-------------------------------------")
            if category == '1': categoryValue = 'Food'
            elif category == '2': categoryValue = 'Utilities'
            elif category == '3': categoryValue = 'Transpo'
            elif category == '4': categoryValue = 'Others'
            for expense in expenses:

                if expense["Category"].lower().strip() == categoryValue.lower():
                    print(f"{expense['Category']}\t{expense['Description']}\t{expense['Amount']}\t{expense['Date']}")
                    found = True
            if not found:
                print(f"No records found for category {category}.")
            else:
                break

def filter_by_amount():
    while True:
        print("\n--- Filter Expenses by Amount ---")
        checker = True
        while checker:
            min_amount = float(input("Enter the minimum amount: [Enter x to go back] > ").strip())
            if 'x' == min_amount: break
            elif not min_amount: print("Invalid min amount. Please try again.")
            max_amount = float(input("Enter the maximum amount: [Enter x to go back] > ").strip())
            if 'x' == max_amount: break
            elif not max_amount: print("Invalid max amount. Please try again.")
            else: checker = False

        found = False
        try:
            print("Category\tDescription\t\tAmount\t   Date")
            print("-------------------------------------")
            for expense in expenses:

                if min_amount <= expense["Amount"] <= max_amount:
                    print(f"{expense['Category']}\t{expense['Description']}\t{expense['Amount']}\t{expense['Date']}")
                    found = True
            if not found:
                print(f"No records found with amounts between {min_amount} and {max_amount}.")
            else:
                break
        except ValueError:
            print("Invalid amount. Please try again.")


def expense_menu():
    while True:
        print("-------------------------------------")
        print("View Expense")
        print("-------------------------------------")
        print("1) View all expenses")
        print("2) Filtered by month")
        print("3) Filtered by category")
        print("4) Filtered by amount")
        print("x) Go Back")
        print("-------------------------------------")

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
        print("-------------------------------------")
        print("Personal Expense Tracker")
        print("-------------------------------------")
        print("1) View Expenses")
        print("x) Exit")
        print("-------------------------------------")

        choice = input("Choose an option > ").strip()

        if choice == '1':
            expense_menu()
        elif choice.lower() == 'x':
            print("Thank you for using Personal Expense Tracker!")
            break
        else:
            print("Invalid option. Please try again.\n")
