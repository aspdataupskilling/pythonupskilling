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

# Function to print expenses in a table format
def print_expenses(expenses: List[ExpenseDetail]):
  # Define the column widths
  category_width = max(len("Category"), max((len(e.category) for e in expenses), default=0))
  description_width = max(len("Description"), max((len(e.description) for e in expenses), default=0))
  amount_width = max(len("Amount"), max((len(e.amount) for e in expenses), default=0))
  date_width = len("Date")

  # Print the header
  header = f"{'Category':<{category_width}} \t {'Description':<{description_width}} \t {'Amount':<{amount_width}} \t {'Date':<{date_width}}"
  print(header)

  # Print each expense
  for expense in expenses:
    print(f"{expense.category:<{category_width}} \t {expense.description:<{description_width}} \t {expense.amount:<{amount_width}} \t {expense.date.strftime('%d/%m/%Y'):<{date_width}}")

# csv_file_path = '/home/eddie_orozco/playground/python/acn/repo/pythonupskilling/expenses.csv'
csv_file_path = 'expenses.csv'
expenses_list = read_csv_to_dto_list(csv_file_path)

# Function to view expenses
def view_expenses():
  try:
    print('------------------------')
    print('View Expenses')
    print('------------------------')
    print('1) View all expenses')
    print('2) Filtered by month')
    print('3) Filtered by category')
    print('4) Filtered by amount')
    print('x) Go Back')
    print('------------------------')
    option = input('Choose an option > ').strip()

    if option == '1':
      view_all_expenses(expenses_list)
    elif option == '2':
      view_expenses_filtered_by_month(expenses_list)
    elif option == '3':
      view_expenses_filtered_by_category(expenses_list)
    elif option == '4':
      view_expenses_filtered_by_amount(expenses_list)
    elif option == 'x':
      personal_expense_tracker_option()
  except ValueError as e:
    logging.error(e)

  pass

# Function to view all expenses
def view_all_expenses(expenses: List[ExpenseDetail]):
  print_expenses(expenses)
  view_expenses()

# Function to filter expenses by month
def filter_by_month(expenses: List[ExpenseDetail], month: int) -> List[ExpenseDetail]:
  return [expense for expense in expenses if expense.date.month == month]

# Function to view expenses filtered by month
def view_expenses_filtered_by_month(expenses: List[ExpenseDetail]):
  try:
    print('------------------------')
    option = input('Enter the month to filter by (1-12). Enter \'x\' to go back > ').strip()
    if option == '1' or option == '2' or option == '3' or option == '4' or option == '5' or option == '6' or option == '7' or option == '8' or option == '9' or option == '10' or option == '11' or option == '12':
      expenses_filtered_by_month = filter_by_month(expenses, int(option))
      print_expenses(expenses_filtered_by_month)
      view_expenses()
    elif option == 'x':
      view_expenses()
  except ValueError as e:
    logging.error(e)

# Function to filter expenses by category
def filter_by_category(expenses: List[ExpenseDetail], category: str) -> List[ExpenseDetail]:
  return [expense for expense in expenses if expense.category == category]

# Function to view expenses filtered by category
def view_expenses_filtered_by_category(expenses: List[ExpenseDetail]):
  try:
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
      expenses_filtered_by_category = filter_by_category(expenses, category)
      print_expenses(expenses_filtered_by_category)
      view_expenses()
    elif option == 'x':
      exit()
  except ValueError as e:
    logging.error(e)

# Function to filter expenses by amount
def filter_by_amount(expenses: List[ExpenseDetail], minAmount: float, maxAmount: float) -> List[ExpenseDetail]:
  return [expense for expense in expenses if float(expense.amount) <= maxAmount and float(expense.amount) >= minAmount]

# Function to view expenses filtered by amount
def view_expenses_filtered_by_amount(expenses: List[ExpenseDetail]):
  try:
    minAmount = input('Enter minimum amount (Enter \'x\' to exit) > ').strip()
    if minAmount == 'x':
      exit()
    maxAmount = input('Enter maximum amount (Enter \'x\' to exit) > ').strip()
    if maxAmount == 'x':
      exit()
    expenses_filtered_by_amount = filter_by_amount(expenses, float(minAmount), float(maxAmount))
    print_expenses(expenses_filtered_by_amount)
    view_expenses()
  except ValueError as e:
    logging.error(e)

# Function to view personal expense tracker option
def personal_expense_tracker_option():
  try:
    print('------------------------')
    print('Personal Expense Tracker')
    print('------------------------')
    print('1) View Expenses')
    print('x) Exit')
    print('------------------------')
    option = input('Choose an option > ').strip()

    if option == '1':
      view_expenses()
    elif option == 'x':
      logging.info("Exiting the program.")
      exit()
  except ValueError as e:
    logging.error(e)

def main_page():
  try:
    personal_expense_tracker_option()

    exit()
  except Exception:
    logging.error('Program error')
    traceback.print_exc()

if __name__ == "__main__":
  main_page()