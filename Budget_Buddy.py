from datetime import datetime, timedelta

def add_expense(expenses_dict, date, category, amount):
    """
    Add an expense to the expenses dictionary.

    Args:
        expenses_dict (dict): Dictionary to store expenses.
        date (str): Date of the expense in the format 'YYYY-MM-DD'.
        category (str): Category of the expense.
        amount (float): Amount of the expense.

    Returns:
        None
    """
    if date not in expenses_dict:
        expenses_dict[date] = []
    expenses_dict[date].append({"category": category, "amount": amount})

def validate_category(category):
    """
    Validate if the given category is one of the predefined categories.

    Args:
        category (str): Category to validate.

    Returns:
        bool: True if the category is valid, False otherwise.
    """
    categories = {
        "Food": True,
        "Travel": True,
        "Shopping": True,
        "Medical": True,
        "Stationary": True,
        "Grocery": True,
        "Bills": True,
        "Other": True
    }
    return categories.get(category, False)

def display_expenses_summary(expenses, monthly_budget):
    """
    Display daily, weekly, and monthly expenses summaries.

    Args:
        expenses (dict): Dictionary containing expenses.
        monthly_budget (float): Monthly budget set by the user.

    Returns:
        None
    """
    # Display daily expenses
    print("\nDaily Expenses Summary:")
    for date, items in sorted(expenses.items()):
        print(f"\nDate: {date}")
        total_daily_expense = sum(item['amount'] for item in items)
        for item in items:
            print(f"{item['category']}: ₹{item['amount']:.2f}")
        print(f"Total expenses for the day: ₹{total_daily_expense:.2f}")

    # Display weekly expenses
    weekly_expenses = {}
    for date, items in expenses.items():
        start_of_week = (datetime.strptime(date, '%Y-%m-%d') - timedelta(days=datetime.strptime(date, '%Y-%m-%d').weekday())).strftime('%Y-%m-%d')
        end_of_week = (datetime.strptime(start_of_week, '%Y-%m-%d') + timedelta(days=6)).strftime('%Y-%m-%d')
        week_range = f"{start_of_week} to {end_of_week}"
        if week_range not in weekly_expenses:
            weekly_expenses[week_range] = []
        weekly_expenses[week_range].extend(items)

    print("\nWeekly Expenses Summary:")
    for week_range, items in sorted(weekly_expenses.items()):
        print(f"\nWeek from {week_range}")
        total_weekly_expense = sum(item['amount'] for item in items)
        for item in items:
            print(f"{item['category']}: ₹{item['amount']:.2f}")
        print(f"Total expenses for the week: ₹{total_weekly_expense:.2f}")

    # Display monthly expenses
    monthly_expenses = {}
    for date, items in expenses.items():
        month = datetime.strptime(date, '%Y-%m-%d').strftime('%m')
        if month not in monthly_expenses:
            monthly_expenses[month] = {}
        for item in items:
            category = item['category']
            amount = item['amount']
            if category not in monthly_expenses[month]:
                monthly_expenses[month][category] = 0
            monthly_expenses[month][category] += amount

    print("\nMonthly Expenses Summary:")
    total_monthly_expense = 0
    for month, categories in sorted(monthly_expenses.items()):
        month_name = datetime.strptime(month, '%m').strftime('%B')
        print(f"\nMonth: {month_name} ({month})")
        for category, amount in categories.items():
            total_monthly_expense += amount
            print(f"{category}: ₹{amount:.2f}")
    print(f"\nTotal expenses for the month: ₹{total_monthly_expense:.2f}")

    # Check if expenses exceed the monthly budget
    if total_monthly_expense > monthly_budget:
        print("\nWarning: Expenses exceed the monthly budget!")

def main():
    print("Categories: Food, Travel, Shopping, Medical, Stationary, Grocery, Bills, Other")

    # Prompt user to set monthly budget
    while True:
        try:
            monthly_budget = float(input("Enter your monthly budget: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    expenses = {}

    while True:
        print("\nEnter expenses for the day (or type 'done' to finish):")
        date_input = input("Enter the date of the expense (YYYY-MM-DD): ")
        if date_input.lower() == 'done':
            break
        
        try:
            date = datetime.strptime(date_input, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            continue

        category = input("Enter the category of the expense: ")
        if not validate_category(category):
            print("Invalid category. Please choose a category from the predefined list.")
            continue

        amount = float(input("Enter the amount of the expense: "))

        add_expense(expenses, date.strftime('%Y-%m-%d'), category, amount)

    display_expenses_summary(expenses, monthly_budget)

if __name__ == "__main__":
    main()