from models import ExpenseTracker, Category  # Import necessary classes
from utils import input_amount, input_date  # Import utility functions

def display_menu():
    print("\nExpense Tracker Menu")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Save Expenses to CSV")
    print("5. Load Expenses from CSV")
    print("6. Generate Report")
    print("7. Manage Categories")
    print("8. Exit")

def manage_categories(category_manager):
    print("\nCategories:", category_manager.list_categories())
    new_category = input("Enter a new category (or press Enter to skip): ").strip()
    if new_category:
        category_manager.add_category(new_category)
        print(f"Added category: {new_category}")

def generate_report(tracker):
    print("\nChoose Report Period:")
    print("1. Daily")
    print("2. Weekly")
    print("3. Monthly")
    choice = input("Select report type (1/2/3): ")

    if choice == "1":
        tracker.generate_report(period="daily")
    elif choice == "2":
        tracker.generate_report(period="weekly")
    elif choice == "3":
        tracker.generate_report(period="monthly")
    else:
        print("Invalid choice. Please try again.")

def main():#It acts as the entry point of the program, where the core logic is executed when the application starts.
    tracker = ExpenseTracker()#This creates an instance of the ExpenseTracker class.tracker is an object that can call methods from the ExpenseTracker class to add, view, delete expenses
    categories = Category()

    tracker.load_from_csv()  # Load saved expenses from CSV

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            amount = input_amount()
            date = input_date()

            # categories is an instance of the Category class (created using categories = Category()).
            # list_categories() method is defined in the Category class to return a list of all categories that have been added by the user.
            print("Categories:", categories.list_categories())

            # .strip():The .strip() method removes any leading or trailing whitespace from the input.
            category = input("Enter category: ").strip()
            description = input("Enter description (optional): ").strip()
            tracker.add_expense(amount, date, category, description)
            print("Expense added successfully.")

        elif choice == "2":
            print("\nAll Expenses:")
            tracker.view_expenses()

        elif choice == "3":
            tracker.view_expenses()
            index = int(input("Enter the index of the expense to delete: "))
            tracker.delete_expense(index)

        elif choice == "4":
            tracker.save_to_csv()
            print("Expenses saved to CSV.")

        elif choice == "5":
            tracker.load_from_csv()
            print("Expenses loaded from CSV.")

        elif choice == "6":
            generate_report(tracker)

        elif choice == "7":
            manage_categories(categories)

        elif choice == "8":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
