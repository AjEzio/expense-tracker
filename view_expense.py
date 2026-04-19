from storage import ensure_data_file
import csv
def view_expense():
    DATA_FILE = ensure_data_file()
    with open(DATA_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)