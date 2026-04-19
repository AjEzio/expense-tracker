from storage import ensure_data_file
from validate_acc import validate_acc
import csv
from datetime import date
def add_expense():
    DATA_FILE = ensure_data_file()
    flag = True
    ex = {}
    default = {
        "date": date.strftime(date.today(),"%d/%m/%Y"),
        "amount": "0",
        "category": "Others",
        "note": "Nil"
    }
    while flag:
        ex["date"] = input("\nEnter the date(DD/MM/YYYY): ").strip() or default["date"]
        ex["amount"] = input("\nEnter the amount: ").strip() or default["amount"]
        ex["category"] = input("\nEnter the category: ").strip() or default["category"]
        ex["note"] = input("\nEnter the note: ").strip() or default["note"]
        ex = validate_acc(ex)
        more_ex = input("\nPress 1 if you want to continue or any other key to exit adding expense: ")
        with open(DATA_FILE, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(ex.values())
        if more_ex != "1":
            flag = False

