from sys import exit
from datetime import datetime
from typing import List

import traceback
import logging
import csv


class ExpenseDetail:
  def __init__(self, category: str, description: str, amount: str, date: datetime):
    self.category = category
    self.description = description
    self.amount = amount
    self.date = date

  def __repr__(self):
    return (f"ExpenseDetail(category={self.category}, description={self.description}, amount={self.amount}, date={self.date.strftime('%d/%m/%Y')})")

# Function to read CSV and convert to list of ExpenseDetail
def read_csv_to_dto_list(file_path: str) -> List[ExpenseDetail]:
  expenses = []

  with open(file_path, mode='r', newline='') as file:
    reader = csv.reader(file)
    next(reader) # Skip the header row
    for row in reader:
      category = row[0]
      description = row[1]
      amount = row[2] # Keep amount as string
      date = datetime.strptime(row[3], "%d/%m/%Y")
      expenses.append(ExpenseDetail(category, description, amount, date))
  
  return expenses

# Function to export filtered expenses to a CSV file
def export_to_csv(filtered_expenses: List[ExpenseDetail], file_name: str):
  with open(file_name, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Category", "Description", "Amount", "Date"]) # Write the header
    for expense in filtered_expenses:
      writer.writerow([expense.category, expense.description, expense.amount, expense.date.strftime('%d/%m/%Y')])

# Function to print expenses in a table format
def print_expenses(expenses: List[ExpenseDetail]):
  # Define the column widths
  category_width = max(len("Category"), max((len(e.category) for e in expenses), default=0))
  description_width = max(len("Description"), max((len(e.description) for e in expenses), default=0))
  amount_width = max(len("Amount"), max((len(e.amount) for e in expenses), default=0))
  date_width = len("Date")

  # Print the header
  header = f"{'Category':<{category_width}} \t {'Description':<{description_width}} \t {'Amount':<{amount_width}} \t {'Date':<{date_width}}"
  print('------------------------')
  print(header)

  # Print each expense
  for expense in expenses:
    print(f"{expense.category:<{category_width}} \t {expense.description:<{description_width}} \t {expense.amount:<{amount_width}} \t {expense.date.strftime('%d/%m/%Y'):<{date_width}}")

csv_file_path = 'expenses.csv'
export_csv_file_path = 'expense_extract.csv'
expenses_list = read_csv_to_dto_list(csv_file_path)

# Function to view expenses
def view_expenses():
  try:
    print('------------------------')
    print('View Expenses')
    print('------------------------')
    print('1) View all expenses')
    print('2) Filtered by date')
    print('3) Filtered by category')
    print('4) Filtered by amount')
    print('x) Go Back')
    print('------------------------')
    option = input('Choose an option > ').strip()

    if option == '1':
      all_expenses(expenses_list, True)
    elif option == '2':
      expenses_filtered_by_date(expenses_list, True)
    elif option == '3':
      expenses_filtered_by_category(expenses_list, True)
    elif option == '4':
      expenses_filtered_by_amount(expenses_list, True)
    elif option == 'x':
      personal_expense_tracker_option()
    else:
      raise ValueError("Invalid option")
  except ValueError as e:
    # logging.error(e)
    print(e)
    view_expenses()

# Function to extract expenses
def extract_expenses():
  try:
    print('------------------------')
    print('Extract Expenses')
    print('------------------------')
    print('1) Extract all expenses')
    print('2) Filtered by date')
    print('3) Filtered by category')
    print('4) Filtered by amount')
    print('x) Go Back')
    print('------------------------')
    option = input('Choose an option > ').strip()

    if option == '1':
      all_expenses(expenses_list, False)
    elif option == '2':
      expenses_filtered_by_date(expenses_list, False)
    elif option == '3':
      expenses_filtered_by_category(expenses_list, False)
    elif option == '4':
      expenses_filtered_by_amount(expenses_list, False)
    elif option == 'x':
      personal_expense_tracker_option()
    else:
      raise ValueError("Invalid option")
  except ValueError as e:
    # logging.error(e)
    print(e)
    extract_expenses()

# Function to all expenses
def all_expenses(expenses: List[ExpenseDetail], isView: bool):
  if (isView):
    print_expenses(expenses)
    view_expenses()
  else:
    export_to_csv(expenses, export_csv_file_path)
    print('------------------------')
    print('expense_extract.csv file created for all expenses')
    extract_expenses()

# Function to filter expenses by date
def filter_by_date(expenses: List[ExpenseDetail], month: int, year: int) -> List[ExpenseDetail]:
  return [expense for expense in expenses if expense.date.month == month]

# Function to expenses filtered by date
def expenses_filtered_by_date(expenses: List[ExpenseDetail], isView: bool):
  try:
    monthOption = input('Enter the month to filter by (1-12). Enter \'x\' to go back > ').strip()
    if monthOption == 'x':
      if (isView):
        view_expenses()
      else:
        extract_expenses()

    yearOption = input('Enter the year from year 1970 onwards. Enter \'x\' to go back > ').strip()
    if yearOption == 'x':
      if (isView):
        view_expenses()
      else:
        extract_expenses()

    if (monthOption == '1' or monthOption == '2' or monthOption == '3' or monthOption == '4' or monthOption == '5' or
        monthOption == '6' or monthOption == '7' or monthOption == '8' or monthOption == '9' or monthOption == '10' or
        monthOption == '11' or monthOption == '12'):
      
      if int(yearOption) >= 1970:
        expenses_filtered = filter_by_date(expenses, int(monthOption), int(yearOption))
        if (isView):
          print_expenses(expenses_filtered)
          view_expenses()
        else:
          export_to_csv(expenses_filtered, export_csv_file_path)
          print('------------------------')
          print('expense_extract.csv file created based on the filter by date')
          extract_expenses()
      else:
        raise ValueError("Invalid year\nTry again")
    else:
      raise ValueError("Invalid month\nTry again")
  except ValueError as e:
    # logging.error(e)
    print(e)
    expenses_filtered_by_date(expenses_list, isView)

# Function to filter expenses by category
def filter_by_category(expenses: List[ExpenseDetail], category: str) -> List[ExpenseDetail]:
  return [expense for expense in expenses if expense.category == category]

# Function to expenses filtered by category
isNotCategoryRetry = True
def expenses_filtered_by_category(expenses: List[ExpenseDetail], isView: bool):
  global isNotCategoryRetry
  try:
    if isNotCategoryRetry:
      print('------------------------')
      print('Filter by Category')
      print('------------------------')
      print('1) Food')
      print('2) Utilities')
      print('3) Transpo')
      print('4) Others')
      print('x) Exit')
      print('------------------------')
    option = input('Choose the category to filter by > ').strip()
    if option == '1' or option == '2' or option == '3' or option == '4':
      category = 'Food' if option == '1' else 'Utilities' if option == '2' else 'Transpo' if option == '3' else 'Others'
      expenses_filtered = filter_by_category(expenses, category)
      isNotCategoryRetry = True
      if (isView):
        print_expenses(expenses_filtered)
        view_expenses()
      else:
        export_to_csv(expenses_filtered, export_csv_file_path)
        print('------------------------')
        print('expense_extract.csv file created based on the filter by category')
        extract_expenses()
    elif option == 'x':
      isNotCategoryRetry = True
      if (isView):
        view_expenses()
      else:
        extract_expenses()
    else:
      raise ValueError("Invalid category")
  except ValueError as e:
    # logging.error(e)
    isNotCategoryRetry = False
    print(e)
    expenses_filtered_by_category(expenses_list, isView)

# Function to filter expenses by amount
def filter_by_amount(expenses: List[ExpenseDetail], minAmount: float, maxAmount: float) -> List[ExpenseDetail]:
  return [expense for expense in expenses if float(expense.amount) <= maxAmount and float(expense.amount) >= minAmount]

# Function to expenses filtered by amount
def expenses_filtered_by_amount(expenses: List[ExpenseDetail], isView: bool):
  try:
    minAmount = input('Enter minimum amount (Enter \'x\' to exit) > ').strip()
    if minAmount == 'x':
      if (isView):
        view_expenses()
      else:
        extract_expenses()
    maxAmount = input('Enter maximum amount (Enter \'x\' to exit) > ').strip()
    if maxAmount == 'x':
      if (isView):
        view_expenses()
      else:
        extract_expenses()
    if float(minAmount) < 0:
      raise ValueError("Invalid amount: Enter amount greater than 0")
    elif float(maxAmount) < 0:
      raise ValueError("Invalid amount: Enter amount greater than 0")
    elif float(minAmount) > float(maxAmount):
      raise ValueError("Invalid amount: Enter maximum amount greater than minimum amount")
    expenses_filtered = filter_by_amount(expenses, float(minAmount), float(maxAmount))
    if (isView):
      print_expenses(expenses_filtered)
      view_expenses()
    else:
      export_to_csv(expenses_filtered, export_csv_file_path)
      print('------------------------')
      print('expense_extract.csv file created based on the filter by amount')
      extract_expenses()
  except ValueError as e:
    # logging.error(e)
    print(e)
    expenses_filtered_by_amount(expenses_list, isView)

# Function to view personal expense tracker option
def personal_expense_tracker_option():
  try:
    print('------------------------')
    print('Personal Expense Tracker')
    print('------------------------')
    print('1) View Expenses')
    print('2) Extract Expenses')
    print('x) Exit')
    print('------------------------')
    option = input('Choose an option > ').strip()

    if option == '1':
      view_expenses()
    elif option == '2':
      extract_expenses()
    elif option == 'x':
      # logging.info("Exiting the program.")
      print('Exiting the program.')
      exit()
    else:
      raise ValueError("Invalid option")
  except ValueError as e:
    # logging.error(e)
    print(e)

def main_page():
  try:
    personal_expense_tracker_option()

    exit()
  except Exception:
    # logging.error('Program error')
    print('Program error')
    traceback.print_exc()

if __name__ == "__main__":
  main_page()