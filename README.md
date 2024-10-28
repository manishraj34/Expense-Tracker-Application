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

<img src="![alt text](image.png)" height="400" width="800">

2. Viewing All Expenses:

Select the "View Expenses" option from the menu to see a list of all expenses.
![image](https://github.com/user-attachments/assets/1a870a0f-0ddc-4afa-87c2-806e8db6cf12 )

3. Deleting an Expenses:

![image](https://github.com/user-attachments/assets/7203cdeb-6d7f-49e5-a62d-2a8085bc2af0)
![image](https://github.com/user-attachments/assets/dc68a1ce-fce0-40ab-812a-defe9c162611)


4. Saving Expenses to CSV:
- The application automatically saves expenses to a CSV file after each session.
- The data is stored in the data/expenses.csv file.
  ![image](https://github.com/user-attachments/assets/6bd2add9-4c1a-4b3e-aaca-4e45fae0dd53)


5. Loading Expenses from CSV:

Upon starting, the application loads previous expenses from the CSV file, so your data is always preserved.
![image](https://github.com/user-attachments/assets/9b45d14c-6a45-4441-89c5-679942f950b5)

6. Generating Reports: 

You can generate reports for daily, weekly, or monthly expenses.
![image](https://github.com/user-attachments/assets/b575d1df-14dd-42a5-8058-fd000d10815f)

## Known Issues
- Date Format: The application currently supports only the YYYY-MM-DD format for dates.
- CSV File Conflicts: If the CSV file is modified manually, it may cause issues when loading expenses.

   




