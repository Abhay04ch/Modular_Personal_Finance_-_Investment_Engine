def add_expense():
    category = input("Enter the category of the item(like food, travel, clothing, etc): ")
    description = input("Enter a short description: ")

    try:
        amount = float(input("Enter the amount spent:"))

        with open("expenses.csv", 'a') as file:
            file.write(f"{category}, {description}, {amount}\n")

    except ValueError:
        print("Invalid input for amount. Please enter a valid number.")


def view_expenses():
    try:
        with open('expenses.csv','r') as file:
            print()
            print("*" * 65)
            print("Category, Description, Amount")
            print("*" * 65)
            total = 0
            for line in file:
                data = line.strip().split(',')

                if len(data) == 3:
                    category, description, amount = data
                    print(f"Category: {category:<15} | {description:<30} | Amount: {amount}")
                    total += float(amount)

                print("*" * 65)
            print(f"Total Expenses: {total}")

    except FileNotFoundError:
        print("No expenses found. Please add some expenses first.")

def search_by_category():
    category_to_be_searched = input("Enter the category you want to search:").strip().lower()

    try:
        with open('expenses.csv', 'r') as file:
            print()
            print('*' * 65)
            print(f"Expenses in category: {category_to_be_searched}")
            print('*' * 65)
            category_total = 0
            for line in file:
                data = line.strip().split(',')
                if len(data) == 3:
                    category, description, amount = data
                    if category.strip().lower() == category_to_be_searched:
                        print(f"{category:<15} | {description:<30} | Amount: {amount}")
                        category_total += float(amount)

            print('*' * 65)
            print(f"Total for category '{category_to_be_searched}': {category_total}")

    except FileNotFoundError:
        print("No data found in the file.")


def main():
    while True:
        print("*" * 65)
        print("This is the tracker App")
        print("*" * 65)
        print("1. Add a new item")
        print("2. View existing items")
        print("3. Search for expenses by category")
        print("4. Exit")
        print("-" * 65)
        print()

        choice = int(input("Enter your choice (1-4): "))

        if choice == 1:
            print("Adding a new expense:")
            add_expense()
            # print()
        elif choice == 2:
            print("Viewing existing items:")
            view_expenses()
            # print()
        elif choice == 3:
            print("Searching for expenses by category:")
            search_by_category()
            # print()
        elif choice == 4:
            print("Exit the tracker app. Thank you for visiting!")
            break
        else:
            print("Invalid choice. Please enter a valid option (1-4).")

if __name__ == "__main__":
    main()

