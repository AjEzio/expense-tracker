from datetime import date,datetime

def validate_acc(ex):
    flag = True
    while flag:
        try:
            ex["date"] = datetime.strptime(ex["date"], "%d/%m/%Y").date()
            flag = False
        except ValueError:
            print("Date must be DD/MM/YYYY")
            ex["date"]=input("\nEnter the date(DD/MM/YYYY): ").strip() or date.today().strftime("%d/%m/%Y")
    ex["date"] = ex["date"].strftime("%d/%m/%Y")
    flag =True
    while flag:
        try:
            ex["amount"] = float(ex["amount"])
            if ex["amount"] < 0:
                print("Amount must be a positive number")
                ex["amount"] = input("\nEnter the amount: ").strip() or "0"
            else:    
                flag = False
        except ValueError:
            print("Amount must be a positive number")
            ex["amount"] = input("\nEnter the amount: ").strip() or "0"

    return ex