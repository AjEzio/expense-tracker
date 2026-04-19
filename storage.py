import csv
from pathlib import Path


DATA_FILE = Path(__file__).parent / "data" / "expenses.csv"


def ensure_data_file():
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    if not DATA_FILE.exists():
        with DATA_FILE.open("w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["date", "amount", "category", "note"])
    return DATA_FILE
