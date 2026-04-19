# Expense Tracker

A small **command-line** expense tracker written in Python. You can add expenses, view them as rows, and see a total—all stored in a simple CSV file.

This project is for **learning practice**. Sample data in the repo is **not real spending**.

## What you need

- **Python 3** installed on your computer ([python.org](https://www.python.org/downloads/) if you need it).
- This project uses Python’s **standard library** only (no extra packages to install).

## How to run it

1. Open a terminal (PowerShell on Windows).
2. Go to this project folder:
   ```bash
   cd path\to\expense_tracker
   ```
3. Start the program:
   ```bash
   python main.py
   ```

## Using the menu

After you run the program, you’ll see a menu:

| Choice | What it does |
|--------|----------------|
| **1** | Add an expense (date, amount, category, note). You can add more than one in a row. |
| **2** | View saved expenses (printed from the CSV). |
| **3** | Show total expense (summary). |
| **4** | Exit the program. |

Type the number and press **Enter**.

## Where your data is saved

Expenses are stored in:

`data/expenses.csv`

The first time you run the app, that file is created automatically with a header row (`date`, `amount`, `category`, `note`).

## Project files (quick map)

| File | Role |
|------|------|
| `main.py` | Starts the app and shows the menu. |
| `add_expense.py` | Adding new rows to the CSV. |
| `view_expense.py` | Showing expenses on screen. |
| `reports.py` | Totals / reporting text. |
| `storage.py` | Makes sure `data/expenses.csv` exists. |
| `validate_acc.py` | Checks input (for example date format). |

## Next steps for you

- Change labels or add a menu option as you learn more Python.
- After editing files, use **Git** to save changes: `git add`, `git commit`, `git push` to update your copy on GitHub.

