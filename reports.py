from storage import ensure_data_file
import csv
def format_total():
    DATA_FILE = ensure_data_file()
    with open(DATA_FILE,"r",newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        total = sum(float(item.get("amount", 0)) for item in reader)
    return f"Total spend: {total:.2f}"
