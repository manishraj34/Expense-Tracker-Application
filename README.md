# Expense-Tracker-Application

## Overview
This Expense Tracker Application is a command-line tool built using Python to help users manage daily expenses. It allows users to add, update, categorize, and delete expenses, generate reports for specific periods, and save/load data using CSV files. The project integrates key concepts like OOP, file handling, and error handling.

## Objectives
- Provide an easy way to track and manage expenses.
- Enable users to assign custom categories to expenses.
- Allow report generation for different periods: daily, weekly, and monthly.
- Ensure data persistence using CSV files across sessions.
- Handle user input errors gracefully to prevent application crashes.

## Setup Instructions
Run the Application:
Navigate to the src folder and run the main file:
- cd src
- python main.py

## Usage Instructions
1. Adding an Expense:

The application will prompt you to enter the amount, date, category, and description.

<img src="https://github.com/user-attachments/assets/ab6a727e-5e9d-4594-85c1-02daef2e2594" height="400" width="800">

2. Viewing All Expenses:

Select the "View Expenses" option from the menu to see a list of all expenses.
<img src="https://github.com/user-attachments/assets/549588a8-49b2-4beb-a15d-fbace66328d0" height="400" width="800">

3. Deleting an Expenses:

<img src="https://github.com/user-attachments/assets/796bae34-4211-4084-b8aa-c9ba023cf435" height="400" width="800">

4. Saving Expenses to CSV:
- The application automatically saves expenses to a CSV file after each session.
- The data is stored in the data/expenses.csv file.
 <img src="https://github.com/user-attachments/assets/516454e7-5a67-4d28-9219-899a747ab5bf" height="400" width="800">


5. Loading Expenses from CSV:

Upon starting, the application loads previous expenses from the CSV file, so your data is always preserved.
<img src="https://github.com/user-attachments/assets/be4424d7-6310-43f3-a945-d3c2e8017452" height="400" width="800">

6. Generating Reports: 

You can generate reports for daily, weekly, or monthly expenses.
<img src="https://github.com/user-attachments/assets/150bc764-9053-413d-bca1-97f12fbdfe10" height="400" width="800">

## Known Issues
- Date Format: The application currently supports only the YYYY-MM-DD format for dates.
- CSV File Conflicts: If the CSV file is modified manually, it may cause issues when loading expenses.

   




