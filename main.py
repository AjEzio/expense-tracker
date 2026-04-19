from add_expense import add_expense
from view_expense import view_expense
from reports import format_total
def main():
    flag = True
    print("Welcome to Expense Tracker\n")
    print("What would you like to do?\n")
    while flag:
        print("1. Add expense\n2. View expense\n3. View total expense\n4. Exit")
        choice = input("Enter here: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expense()
        elif choice == "3":
            print(format_total())
        elif choice == "4":
            flag = False
        else:
            print("Please pick the given choices")
        print("\n")

    



    


if __name__ == "__main__":
    main()
