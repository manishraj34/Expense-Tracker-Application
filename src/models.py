import csv
from datetime import datetime,timedelta

class Expense:
    def __init__(self, amount, date, category, description=""):
        self.amount = float(amount)
        # Ensure the date is properly handled
        if isinstance(date, str):# If the date is a string, convert it to a date object
            self.date = datetime.strptime(date, "%Y-%m-%d").date()
        elif isinstance(date, datetime):# If the input is a datetime object, extract the date part
            self.date = date.date()
        else:# If already a date object, assign it directly
            self.date = date  # If already a datetime.date object

        self.category = category
        self.description = description

# The __str__() method provides a human-friendly string representation of the expense object, making it easy to understand when printed. 
# In your case, it neatly formats the date, category, amount, and description of an expense in one line.
# Without __str__(), Python prints the memory address of the object, which isn’t helpful.Output: <__main__.Expense object at 0x7f45d5b9d5e0>

    def __str__(self):
        return f"{self.date.strftime('%Y-%m-%d')} - {self.category}: {self.amount} | {self.description}"

class Category:
    def __init__(self):
        self.categories = ["Groceries", "Utilities", "Entertainment"]

    def add_category(self, new_category):
        if new_category not in self.categories:
            self.categories.append(new_category)

    def list_categories(self):
        return self.categories

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, date, category, description=""):
        expense = Expense(amount, date, category, description)
        self.expenses.append(expense)

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded yet.")
        for expense in self.expenses:
            print(expense)

    def delete_expense(self, index):
        try:
            removed = self.expenses.pop(index)
            print(f"Deleted: {removed}")
        except IndexError:
            print("Invalid index. Please try again.")

    def save_to_csv(self, filename="data/expenses.csv"):#filename="data/expenses.csv" sets the default file path where the CSV file will be saved. If no filename is provided when the function is called, it will default to "data/expenses.csv".
        with open(filename, "w", newline="") as file:#newline="" ensures that no extra blank lines are added between rows in the CSV file
            # with ensures the file is automatically closed after the operation completes, even if an error occurs.
            writer = csv.writer(file)
            writer.writerow(["Amount", "Date", "Category", "Description"])
            for expense in self.expenses:
                writer.writerow([
                    expense.amount,
                    expense.date.strftime("%Y-%m-%d"),
                    expense.category,
                    expense.description
                ])

    def load_from_csv(self, filename="data/expenses.csv"):
        try:
            with open(filename, "r") as file:
                reader = csv.DictReader(file)
                # for row in reader:
                #     self.add_expense(row["Amount"], row["Date"], row["Category"], row["Description"])
        except FileNotFoundError:
            print("No existing expense data found. Starting fresh.")

    def generate_report(self, period="daily"):
        """Generate report for daily, weekly, or monthly periods."""
        if not self.expenses:
            print("No expenses to generate a report.")
            return

        today = datetime.today().date()
        total = 0.0

        if period == "daily":
            report_date = today
            print(f"\nReport for {report_date}:")
            for expense in self.expenses:
                if expense.date == report_date:
                    print(expense)
                    total += expense.amount

        elif period == "weekly":
            start_of_week = today - timedelta(days=today.weekday())  # Monday of this week
            print(f"\nWeekly Report (starting {start_of_week}):")
            for expense in self.expenses:
                if start_of_week <= expense.date <= today:
                    print(expense)
                    total += expense.amount

        elif period == "monthly":
            print(f"\nMonthly Report for {today.strftime('%B %Y')}:")
            for expense in self.expenses:
                if expense.date.year == today.year and expense.date.month == today.month:
                    print(expense)
                    total += expense.amount

        print(f"Total Expenses: {total:.2f}")

