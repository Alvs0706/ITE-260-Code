accounts = []
logged_in = False
current_account = []
categories = ["Food", "Transportation", "School Supplies", "Others"]

def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("INVALID INPUT! TRY AGAIN.")

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("INVALID INPUT! TRY AGAIN.")

def start_menu():
    print("================SIGN IN================")
    print("1. Login")
    print("2. Register")
    print("---------------------------------------")
    print("0. Exit")

def registration(accounts):
    def register_student_id():
        while True:
            enter_student_id = input("Student ID (0x-xxxx-xxxxxx): ")
            valid = True
            position = 0
            hyphens = 0

            for character in enter_student_id:
                if character == "-":
                    hyphens = hyphens + 1
                elif character < "0" or character > "9":
                    valid = False
                position = position + 1

            if hyphens == 2 and (position == 13 or position == 14):
                if enter_student_id[0:1] == "0" and enter_student_id[2:3] == "-":
                    if enter_student_id[7:8] == "-":
                        duplicate = False
                        for account in accounts:
                            if enter_student_id == account[0]:
                                duplicate = True

                        if duplicate:
                            print("---------------------------------------")
                            print("STUDENT ID ALREADY REGISTERED.")
                        elif valid:
                            return enter_student_id
                        else:
                            print("---------------------------------------")
                            print("INVALID STUDENT ID. TRY AGAIN.")
                    else:
                        print("---------------------------------------")
                        print("INVALID STUDENT ID. TRY AGAIN.")
                else:
                    print("---------------------------------------")
                    print("INVALID STUDENT ID. TRY AGAIN.")
            else:
                print("---------------------------------------")
                print("INVALID STUDENT ID. TRY AGAIN.")

    def register_password():
        print("---------------------------------------")
        while True:
            enter_password = input("Password (8 characters min.): ")
            if len(enter_password) >= 8:
                return enter_password
            print("PASSWORD MUST BE AT LEAST 8 CHARACTERS.")

    print("===============SIGN UP=================")
    student_id = register_student_id()
    password = register_password()

    while True:
        choice = input("Create this account? (Y/N): ")
        if choice == "Y" or choice == "y":
            accounts.append([student_id, password, []])
            print("---------------------------------------")
            print("ACCOUNT REGISTERED SUCCESSFULLY.")
            return accounts
        elif choice == "N" or choice == "n":
            print("---------------------------------------")
            print("REGISTRATION CANCELLED.")
            return accounts
        else:
            print("INVALID ANSWER! TRY AGAIN.")

def login(accounts):
    print("=================LOGIN=================")
    while True:
        choice = input("Continue to login? (Y/N): ")
        if choice == "Y" or choice == "y":
            print("---------------------------------------")
            enter_id = input("Student ID: ")
            enter_password = input("Password: ")

            for account in accounts:
                if enter_id == account[0] and enter_password == account[1]:
                    print("---------------------------------------")
                    print("LOGIN SUCCESSFUL!")
                    return account
            print("---------------------------------------")
            print("INCORRECT STUDENT ID OR PASSWORD.")
            return False
        elif choice == "N" or choice == "n":
            return False
        else:
            print("INVALID ANSWER!")

def menu(student_id, current_month):
    print("=======================================")
    print("              SpendTrack               ")
    print(f"    Student ID: {student_id}      ")
    print(f"    Current Month: {current_month}")
    print("==============MAIN MENU================")
    print("1. Add Expense")
    print("2. Record Allowance")
    print("3. Set Monthly Budget")
    print("4. View Expenses")
    print("5. Search Expense")
    print("6. Manage Expense")
    print("7. View Expense Summary")
    print("8. Switch Month")
    print("0. Log Out")
    print("---------------------------------------")


def select_month(monthly_records):
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]

    print("============SELECT MONTH============")
    n = 1
    for month in months:
        print(f"{n}. {month}")
        n = n + 1

    while True:
        num = get_int_input("Select month (1-12): ")
        if num >= 1 and num <= 12:
            break
        print("INVALID MONTH!")

    while True:
        year = get_int_input("Enter year: ")
        if year >= 2000:
            break
        print("INVALID YEAR!")

    month_name = months[num - 1]
    for record in monthly_records:
        if record[0] == month_name and record[1] == year:
            print(f"SELECTED: {month_name} {year}")
            return record

    new_record = [month_name, year, [], 0, [0, 0, 0, 0]]
    monthly_records.append(new_record)
    print(f"CREATED RECORD FOR {month_name.upper()} {year}.")
    return new_record

def addexpense(expenses):
    def addnewexpense():
        print("---------------------------------------")
        while True:
            expense = input("Expense Details: ")
            if expense != "":
                break
            print("EXPENSE DETAILS CANNOT BE EMPTY.")

        while True:
            amount = get_float_input("Amount: ₱")
            if amount >= 1:
                break
            print("AMOUNT CANNOT BE LESS THAN 1.")

        print("Categories:")
        print("1. Food")
        print("2. Transportation")
        print("3. School Supplies")
        print("4. Others")

        while True:
            category = get_int_input("Select category (1-4): ")
            if category >= 1 and category <= 4:
                return [expense, amount, categories[category - 1]]
            print("---------------------------------------")
            print("INVALID CATEGORY. TRY AGAIN.")
    new_expense = addnewexpense()

    print("---------------------------------------")
    print(f"Expense Details: {new_expense[0]}")
    print(f"Amount: ₱{new_expense[1]}")
    print(f"Category: {new_expense[2]}")
    print("---------------------------------------")

    while True:
        choice = input("Add this expense? (Y/N): ")
        if choice == "Y" or choice == "y":
            expenses.append(new_expense)
            print("---------------------------------------")
            print("EXPENSE ADDED!")
            print("---------------------------------------")
            return expenses
        elif choice == "N" or choice == "n":
            print("---------------------------------------")
            print("EXPENSE NOT ADDED.")
            print("---------------------------------------")
            return expenses
        else:
            print("INVALID ANSWER! TRY AGAIN.")

def record_allowance(allowance):
    print("========RECORD ALLOWANCE=========")
    print(f"Allowance: ₱{allowance}")
    print("---------------------------------------")

    while True:
        addallowance = get_float_input("Enter amount: ₱")
        if addallowance >= 0:
            allowance = allowance + addallowance
            print("ALLOWANCE ADDED!")
            return allowance
        else:
            print("INVALID NUMBER!")

def monthly_budget(budgets):
    while True:
        print("============MONTHLY BUDGET=============")
        n = 1
        for category in categories:
            if budgets[n - 1] == 0:
                print(f"{n}. {category}: Not set")
            else:
                print(f"{n}. {category}: ₱{budgets[n - 1]}")
            n = n + 1
        print("0. Go back")

        num = get_int_input("Select a category: ")
        if num == 0:
            return budgets
        elif num >= 1 and num <= 4:
            while True:
                amount = get_float_input(f"Enter monthly budget for {categories[num - 1]}: ₱")
                if amount >= 1:
                    budgets[num - 1] = amount
                    print("MONTHLY BUDGET UPDATED!")
                    break
                print("BUDGET CANNOT BE LESS THAN 1.")
        else:
            print("INVALID NUMBER!")

def viewexpense(expenses):
    def viewexpense_menu(expenses):
        n = 0
        print("=============VIEW EXPENSES=============")

        if expenses:
            for expense in expenses:
                print(f"{n + 1}. {expense[0]}, ₱{expense[1]}, {expense[2]}")
                n = n + 1
        else:
            print("No expenses recorded.")
        print("---------------------------------------")
        print("0. Go back")

    while True:
        viewexpense_menu(expenses)
        num = get_int_input("Enter a number: ")

        if num == 0:
            return
        else:
            print("Invalid number!")

def searchexpense(expenses):
    def search(expenses):
        print("============SEARCH EXPENSE=============")
        print("0. Go back")

        while True:
            find = input("Search expense name: ")

            if find == "0":
                return
            found = False
            print("---------------------------------------")
            n = 0

            for expense in expenses:
                if find.lower() in expense[0].lower():
                    print(f"{n + 1}. {expense[0]}, ₱{expense[1]}, {expense[2]}")
                    found = True
                n = n + 1
            if not found:
                print("EXPENSE NOT FOUND.")
            print("---------------------------------------")
    search(expenses)

def manageexpense(expenses):
    def manage_menu():
        print("=============MANAGE EXPENSE============")
        print("1. Update Expense")
        print("2. Delete Expense")
        print("---------------------------------------")
        print("0. Go back")

    def updateexpense(expenses):
        while True:
            n = 0
            print("-------------UPDATE EXPENSE------------")
            print("List of Expenses:")
            if expenses:
                for expense in expenses:
                    print(f"{n + 1}. {expense[0]}")
                    n = n + 1
            else:
                print("No expenses recorded.")
            print("---------------------------------------")
            num = get_int_input("Select Expense: ")

            if num == 0:
                return
            elif num >= 1 and num <= n:
                index = num - 1
                index_selected = expenses[index]
                while True:
                    print("---------------------------------------")
                    print(f"Selected Expense: {index_selected}")
                    print("---------------------------------------")
                    print("1. Expense Details")
                    print("2. Amount")
                    print("3. Category")
                    print("---------------------------------------")
                    print("0. Go back")
                    select = get_int_input("Select a number to modify: ")
                    print("---------------------------------------")

                    if select == 0:
                        return
                    elif select == 1:
                        while True:
                            new_value = input("New expense details: ")
                            if new_value != "":
                                break
                            print("EXPENSE DETAILS CANNOT BE EMPTY.")
                        print("---------------------------------------")
                        print(f"New Expense Details: {new_value}")
                        while True:
                            choice = input("Update this expense? (Y/N): ")
                            if choice == "Y" or choice == "y":
                                index_selected[0] = new_value
                                print("---------------------------------------")
                                print("EXPENSE UPDATED SUCCESSFULLY!")
                                break
                            elif choice == "N" or choice == "n":
                                print("---------------------------------------")
                                print("EXPENSE NOT UPDATED.")
                                break
                            else:
                                print("INVALID ANSWER! TRY AGAIN.")
                    elif select == 2:
                        while True:
                            new_value = get_float_input("New amount: ₱")
                            if new_value >= 1:
                                break
                            print("AMOUNT CANNOT BE LESS THAN 1.")
                        print("---------------------------------------")
                        print(f"New Amount: ₱{new_value}")
                        while True:
                            choice = input("Update this expense? (Y/N): ")
                            if choice == "Y" or choice == "y":
                                index_selected[1] = new_value
                                print("---------------------------------------")
                                print("EXPENSE UPDATED SUCCESSFULLY!")
                                break
                            elif choice == "N" or choice == "n":
                                print("---------------------------------------")
                                print("EXPENSE NOT UPDATED.")
                                break
                            else:
                                print("INVALID ANSWER! TRY AGAIN.")
                    elif select == 3:
                        print("Categories:")
                        print("1. Food")
                        print("2. Transportation")
                        print("3. School Supplies")
                        print("4. Others")
                        while True:
                            category = get_int_input("Select category (1-4): ")
                            if category >= 1 and category <= 4:
                                new_value = categories[category - 1]
                                break
                            print("INVALID CATEGORY. TRY AGAIN.")
                        print("---------------------------------------")
                        print(f"New Category: {new_value}")
                        while True:
                            choice = input("Update this expense? (Y/N): ")
                            if choice == "Y" or choice == "y":
                                index_selected[2] = new_value
                                print("---------------------------------------")
                                print("EXPENSE UPDATED SUCCESSFULLY!")
                                break
                            elif choice == "N" or choice == "n":
                                print("---------------------------------------")
                                print("EXPENSE NOT UPDATED.")
                                break
                            else:
                                print("INVALID ANSWER! TRY AGAIN.")
                    else:
                        print("INVALID NUMBER!")
            else:
                print("INVALID NUMBER!")

    def deleteexpense(expenses):
        while True:
            n = 0
            print("------------DELETE EXPENSE-------------")
            print("List of Expenses:")
            if expenses:
                for expense in expenses:
                    print(f"{n + 1}. {expense[0]}, ₱{expense[1]}, {expense[2]}")
                    n = n + 1
            else:
                print("No expenses recorded.")
            print("---------------------------------------")
            print("0. Go back")
            num = get_int_input("Select Expense: ")

            if num == 0:
                return
            elif num >= 1 and num <= n:
                index = num - 1
                expenses.remove(expenses[index])
                print("---------------------------------------")
                print("EXPENSE SUCCESSFULLY DELETED!")
            else:
                print("INVALID NUMBER!")

    while True:
        manage_menu()
        num = get_int_input("Enter a number (0-2): ")
        if num == 0:
            return
        elif num == 1:
            updateexpense(expenses)
        elif num == 2:
            deleteexpense(expenses)
        else:
            print("INVALID NUMBER!")

def viewsummary(allowance, expenses, budgets):
    def viewsummary_menu(allowance, expenses, budgets):
        print("""=========VIEW EXPENSE SUMMARY==========
""")
        print(f"Current Allowance | ₱{allowance}")
        total_expense = 0

        for expense in expenses:
            total_expense = total_expense + expense[1]
        print(f"Total Expenses | ₱{total_expense}")
        remaining = allowance - total_expense
        print(f"""Remaining Allowance | ₱{remaining}
""")
        expense_categories = []
        print("""----------EXPENSE CATEGORIES:----------
""")

        if expenses:
            for expense in expenses:
                category = expense[2]
                if category not in expense_categories:
                    category_total = 0
                    for expense in expenses:
                        if expense[2] == category:
                            category_total = category_total + expense[1]

                    expense_categories.append(category)
                    print(f"{category} | ₱{category_total}")
        else:
            print("""No expenses recorded.
""")
        print("")
        print("--------CATEGORY BUDGET SUMMARY--------")
        for category_index in range(4):
            category = categories[category_index]
            category_total = 0
            for expense in expenses:
                if expense[2] == category:
                    category_total = category_total + expense[1]
            print(f"{category} | Spent: ₱{category_total}")
            if budgets[category_index] == 0:
                print("Budget: Not set")
            else:
                remaining_budget = budgets[category_index] - category_total
                print(f"Budget: ₱{budgets[category_index]}")
                print(f"Budget remaining: ₱{remaining_budget}")
                if remaining_budget < 0:
                    print("WARNING: BUDGET EXCEEDED!") 
            print("""
---------------------------------------""")
        print("0. Go back")

        while True:
            num = get_int_input("Enter a number: ")

            if num == 0:
                return
            else:
                print("INVALID NUMBER!")
    viewsummary_menu(allowance, expenses, budgets)

while True:
    start_menu()
    num = get_int_input("Enter a number (0-2): ")
    if num == 0:
        print("PROGRAM EXITED")
        break
    elif num == 1:
        current_account = login(accounts)
        if current_account:
            logged_in = True
            monthly_records = current_account[2]
            current_record = select_month(monthly_records)
            current_month = current_record[0] + " " + str(current_record[1])
            expenses = current_record[2]
            allowance = current_record[3]
            budgets = current_record[4]
    elif num == 2:
        accounts = registration(accounts)
    else:
        print("INVALID NUMBER!")

    if logged_in:
        while True:
            menu(current_account[0], current_month)
            num = get_int_input("Enter a number (0-8): ")
            if num == 1:
                expenses = addexpense(expenses)
            elif num == 2:
                allowance = record_allowance(allowance)
            elif num == 3:
                budgets = monthly_budget(budgets)
            elif num == 4:
                viewexpense(expenses)
            elif num == 5:
                searchexpense(expenses)
            elif num == 6:
                manageexpense(expenses)
            elif num == 7:
                viewsummary(allowance, expenses, budgets)
            elif num == 8:
                current_record[2] = expenses
                current_record[3] = allowance
                current_record[4] = budgets
                current_record = select_month(monthly_records)
                current_month = current_record[0] + " " + str(current_record[1])
                expenses = current_record[2]
                allowance = current_record[3]
                budgets = current_record[4]
            elif num == 0:
                print("LOGGED OUT!")
                break
            else:
                print("INVALID NUMBER!")
        current_record[2] = expenses
        current_record[3] = allowance
        current_record[4] = budgets
        current_account[2] = monthly_records
        logged_in = False