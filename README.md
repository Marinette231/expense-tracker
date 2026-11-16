# Expense Tracker
A Python-based command-line Expense Tracker that helps users record, manage, and monitor their daily expenses.

## Features
- **Add Expenses:** Record expense names, amounts, and categories.
- **Input Validation:** Prevent invalid or negative expense amounts.
- **View Expenses:** Display all recorded expenses along with their dates and categories.
- **Category Filtering:** Filter expenses by categories such as Food, Travel, and Shopping.
- **Monthly Summary:** Calculate total expenses for a selected month.
- **Data Persistence:** Automatically save expenses using JSON so records remain available after restarting the application.
- **Error Handling:** Handle missing or corrupted JSON files and missing fields in older expense records.

## Technologies Used
- Python 3
- JSON
- Python DateTime Module

## Project Structure
```text
expense-tracker/
│
├── expense_tracker.py
├── expenses.json
├── README.md
└── .gitignore
```


## How to Run
1. Clone or download this repository.
2. Make sure Python 3 is installed.
3. Open a terminal in the project folder.
4. Run:
```bash
python expense_tracker.py
```

## Application Menu
```text
=== Expense Tracker ===

1. Add Expense
2. View Expenses
3. Filter by Category
4. Monthly Expense Summary
5. Exit
```

## What I Learned
Through this project, I practised:
- Python functions and loops
- Lists and dictionaries
- Exception handling
- File handling
- JSON data storage
- User input validation
- Date handling
- Conditional statements

## Future Improvements
- Category-wise monthly reports
- Graphical user interface
- Database integration using SQLite
- Expense visualization and analytics

## Author
Developed as a Python programming and portfolio project.
