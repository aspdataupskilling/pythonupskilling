from sys import exit

import traceback
import pandas as pd

# Function to filter the DataFrame
def filter_expenses(df=None, category=None, month=None, year=None, min_amount=None, max_amount=None):
    filtered_df = df

    # Filter by category
    if category:
        filtered_df = filtered_df[filtered_df['Category'] == category]

    # Filter by month and year
    if month and year:
        filtered_df = filtered_df[(filtered_df['Date'].dt.month == month) & (filtered_df['Date'].dt.year == year)]

    # Filter by amount range
    if min_amount is not None:
        filtered_df = filtered_df[filtered_df['Amount'] >= min_amount]
    if max_amount is not None:
        filtered_df = filtered_df[filtered_df['Amount'] <= max_amount]

    return filtered_df

def view_expenses(extract = None):
  # Implement view_expenses here
    try:
        file_path = 'expenses.csv'
        df = pd.read_csv(file_path)
        df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')
    except:
        print('Error File Path')
        exit()

    print('-------------------------')
    if extract is False:
        print('View Expenses')
        print('-------------------------')
        print('1) View all expenses')
    else:
        print('Extract Expenses')
        print('-------------------------')
        print('1) Extract all expenses')
    print('2) Filtered by date')
    print('3) Filtered by category')
    print('4) Filtered by amount')
    print('x) Go back')
    print('-------------------------')
    option = input('Choose an option > ')
    if option == '1':
        if extract is False:
            print(df)
        else:
            save_to_csv(df,'for all expenses')

    elif option == '2':
        while True:
            op2Month = input("Enter the month to filter by (1-12). Enter 'x' to go back > ")
            op2Year = input("Enter the year to filter from year 1970 onwards. Enter 'x' to go back > ")

            if op2Month == 'x' or  op2Year == 'x':
                view_expenses(extract)
                break

            try:
                op2Month = int(op2Month)
                if op2Month < 1 or op2Month > 12:
                    print('Invalid month: ', op2Month)
                    print('Try again')
                    continue
            except ValueError:
                print('Invalid month: ', op2Month)
                print('Try again')
                continue

            try:
                op2Year = int(op2Year)
                if op2Year < 1970:
                    print('Invalid year: ', op2Year)
                    print('Try again')
                    continue
            except:
                print('Invalid year: ', op2Year)
                print('Try again')
                continue

            filtered_data = filter_expenses(df=df,month=op2Month,year=op2Year)
            if extract is False:
                print(filtered_data)
            else:
                save_to_csv(filtered_data,'based on the filter by date')
            break

    elif option == '3':
        print('-------------------------')
        print('Filter by Category')
        print('-------------------------')
        print('1) Food')
        print('2) Utilities')
        print('3) Transpo')
        print('4) Others')
        print('x) Exit')
        print('-------------------------')
        while True:
            op3In = input('Choose the category to filter by > ')
            if op3In == 'x':
                view_expenses(extract)
                break
            else:
                if op3In == '1': op3In = "Food"
                elif op3In == '2': op3In = "Utilities"
                elif op3In == '3': op3In = "Transpo"
                elif op3In == '4': op3In = "Others"
                else:
                    print('Invalid Category')
                    continue
                filtered_data = filter_expenses(df=df,category=op3In)
                if extract is False:
                    print(filtered_data)
                else:
                    save_to_csv(filtered_data,'based on the filter by category')
                break

    elif option == '4':
        while True:
            op4InMin = input("Enter minimum amount (Enter 'x' to exit ) > ")
            op4InMax = input("Enter maximum amount (Enter 'x' to exit ) > ")
            if op4InMin == 'x' or op4InMax == 'x':
                view_expenses(extract)
                break
            try:
                op4InMin = int(op4InMin)
                if op4InMin < 0:
                    print('Invalid amount, please enter minimum amount greater than 0')
                    continue
            except ValueError:
                print('Invalid amount, please enter minimum amount greater than 0')
                continue
            try:
                op4InMax = int(op4InMax)
                if op4InMax < 0:
                    print('Invalid amount, please enter maximum amount greater than 0')
                    continue
            except ValueError:
                print('Invalid amount, please enter maximum amount greater than 0')
                continue

            if (op4InMin > op4InMax):
                print('Invalid amount, please enter minimum amount greater than maximum amount')
                continue

            filtered_data = filter_expenses(df=df, min_amount=op4InMin, max_amount=op4InMax)
            if extract is False:
                print(filtered_data)
            else:
                save_to_csv(filtered_data,'based on the filter by amount')
            break

    elif option == 'x':
        main_page()

    else:
        print('\n---- Invalid Option ----\n')
    view_expenses(extract)


def save_to_csv(data, text):
    file_name = 'expense_extract.csv'
    data.to_csv(file_name, index=False)
    print(f"{file_name} file created {text}")

def main_page():
  exitFlag = False
  try:
    # Implement main page here
    while exitFlag is False:
        print('-------------------------')
        print('Personal Expense Tracker')
        print('-------------------------')
        print('1) View Expenses')
        print('2) Extract Expenses')
        print('x) Exit')
        print('-------------------------')
        option = input('Choose an option > ')
        if option == '1':
            view_expenses(extract = False)
        elif option == '2':
            view_expenses(extract = True)
        elif option == 'x':
            exitFlag = True
            print('Exiting...')
        else:
            print('\n---- Invalid Option ----\n')

    exit()
  except Exception:
    print('Program error')
    traceback.print_exc()
