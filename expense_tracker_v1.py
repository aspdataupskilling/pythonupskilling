from sys import exit

import traceback
import pandas as pd

# Function to filter the DataFrame
def filter_expenses(df=None, category=None, month=None, min_amount=None, max_amount=None):
    filtered_df = df

    # Filter by category
    if category:
        filtered_df = filtered_df[filtered_df['Category'] == category]

    # Filter by month
    if month:
        filtered_df = filtered_df[filtered_df['Date'].dt.month == month]

    # Filter by amount range
    if min_amount is not None:
        filtered_df = filtered_df[filtered_df['Amount'] >= min_amount]
    if max_amount is not None:
        filtered_df = filtered_df[filtered_df['Amount'] <= max_amount]

    return filtered_df

def view_expenses():
  # Implement view_expenses here
    try:
        file_path = 'expenses.csv'
        df = pd.read_csv(file_path)
        df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')
    except:
        print('Error File Path')
        exit()

    print('-------------------------')
    print('View Expenses')
    print('-------------------------')
    print('1) View all expenses')
    print('2) Filtered by month')
    print('3) Filtered by category')
    print('4) Filtered by amount')
    print('x) Go back')
    print('-------------------------')
    option = input('Choose an option > ')
    if option == '1':
        print(df)
    elif option == '2':
        op2In = input("Enter the month to filter by (1-12). Enter 'x' to go back > ")
        if op2In == 'x':
            view_expenses()
        else:
            filtered_data = filter_expenses(df=df,month=int(op2In))
            print(filtered_data)
    elif option == '3':
        print('-------------------------')
        print('Filter by Category')
        print('-------------------------')
        print('1) Food')
        print('2) Utilities')
        print('3) Transpo')
        print('4) Others')
        print('x) Exit')
        op3In = input('Choose the category to filter by > ')
        if op3In == 'x':
            view_expenses()
        else:
            if op3In == '1': op3In = "Food"
            elif op3In == '2': op3In = "Utilities"
            elif op3In == '3': op3In = "Transpo"
            elif op3In == '4': op3In = "Others"
            filtered_data = filter_expenses(df=df,category=op3In)
            print(filtered_data)
    elif option == '4':
        op4InMin = input("Enter minimum amount (Enter 'x' to exit > ")
        op4InMax = input("Enter maximum amount (Enter 'x' to exit > ")
        if op4InMin == 'x' or op4InMax == 'x':
            view_expenses()
        else:
            filtered_data = filter_expenses(df=df, min_amount=int(op4InMin), max_amount=int(op4InMax))
            print(filtered_data)
    elif option == 'x':
        main_page()
    view_expenses()

def main_page():
  exitFlag = False
  try:
    # Implement main page here
    while exitFlag is False:
        print('-------------------------')
        print('Personal Expense Tracker')
        print('-------------------------')
        print('1) View Expenses')
        print('x) Exit')
        print('-------------------------')
        option = input('Choose an option > ')
        if option == '1':
            print(option)
            view_expenses()
        elif option == 'x':
            exitFlag = True
            print('Exiting...')
    exit()
  except Exception:
    print('Program error')
    traceback.print_exc()
