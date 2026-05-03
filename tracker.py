import datetime

class Expense:
    def __init__(self, category, description, amount, date=None):
        self.category = category
        self.description = description
        self.amount = amount
        self.date = date if date else datetime.date.today().strftime("%Y-%m-%d")

    def to_csv(self):
        return f"{self.date}, {self.category}, {self.description}, {self.amount}\n"

class Tracker:
    def __init__(self, filename = "expenses.csv"):
        self.filename = filename
        self.expenses = []
        self.load_from_file()

    def add_expense(self, expense_obj):
        self.expenses.append(expense_obj)
        self.save_to_file(expense_obj)

    def save_to_file(self, expense_obj):
        with open(self.filename, 'a') as file:
            file.write(expense_obj.to_csv() + "\n")

    def load_from_file(self):
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) == 4:
                        date, category, description, amount = parts
                        new_expense = Expense(category, description, amount, date)
                        self.expenses.append(new_expense)


        except FileNotFoundError:
            print("No such file exists. You can create one by adding an expense.")


    def view_expenses(self):
        print()
        print("*" * 65)
        print("Date, Category, Description, Amount")
        print("*" * 65)
        total = 0
        for expense in self.expenses:
            print(f"{expense.date}, {expense.category}, {expense.description}, {expense.amount}")
            total += float(expense.amount)

        print("*" * 65)
        print(f"Total Expenses: {total}")

def main():

    tracker = Tracker()

    while True:
        print("\n" + "*" * 65)
        print("PERSONAL FINANCE APP")
        print("*" * 65)
        print("1. Add a new item")
        print("2. View existing items")
        # print("3. Search for expenses by category")
        print("3. Exit")
        print("-" * 65)
        print()

        try:
            choice = int(input("Enter your choice (1-3): "))

            if choice == 1:
                print("Adding a new expense:")
                tracker.add_expense()
                # print()
            elif choice == 2:
                print("Viewing existing items:")
                tracker.view_expenses()
                # print()
            # elif choice == 3:
            #     print("Searching for expenses by category:")
            #     search_by_category()
                # print()
            elif choice == 3:
                print("Exit the tracker app. Thank you for visiting!")
                break
            else:
                print("Invalid choice. Please enter a valid option (1-3).")

        except ValueError:
            print("Invalid Input.")

if __name__ == "__main__":
    main()

