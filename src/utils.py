from datetime import datetime

def input_date(prompt="Enter date (YYYY-MM-DD): "):
    while True:
        date_str = input(prompt)
        try:
            return datetime.strptime(date_str, "%Y-%m-%d").date() # The datetime.strptime() method in Python is used to convert a date and time represented as a string into a datetime object.
        except ValueError:
            print("Invalid date format. Please try again.")

def input_amount(prompt="Enter amount: "):
    while True:
        try:
            amount = float(input(prompt))
            if amount < 0:
                raise ValueError
            return amount
        except ValueError:
            print("Invalid amount. Please enter a positive number.")
