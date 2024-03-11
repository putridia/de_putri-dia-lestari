import uuid

expenses = {}

def add_expense():
    id = str(uuid.uuid4())
    name = input("Enter expense name: ")
    amount = float(input("Enter expense amount: "))
    expenses[id] = {"name": name, "amount": amount}
    print("Data added!")

def view_expenses():
    total = 0
    for id, expense in expenses.items():
        print(f"ID: {id}, Name: {expense['name']}, Amount: {expense['amount']}")
        total += expense['amount']
    print(f"Total expenses: {total}")

def update_expense():
    id = input("Enter expense ID to update: ")
    if id in expenses:
        name = input("Enter new expense name: ")
        amount = float(input("Enter new expense amount: "))
        expenses[id] = {"name": name, "amount": amount}
        print("Data updated!")
    else:
        print("Expense not found.")

def delete_expense():
    id = input("Enter expense ID to delete: ")
    if id in expenses:
        del expenses[id]
    else:
        print("Expense not found.")

while True:
    print("\nMenu:")
    print("===========================")
    print("1. Create new expense data")
    print("2. View expenses")
    print("3. Update expense")
    print("4. Delete expense")
    print("5. Exit")
    print("===========================")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_expense()
    elif choice == 2:
        view_expenses()
    elif choice == 3:
        update_expense()
    elif choice == 4:
        delete_expense()
    elif choice == 5:
        confirm = input("Are you sure you want to exit? (y/n) ")
        if confirm.lower() == "y":
            print("Bye!")
            break
        else:
            print("Cancelled.")
    else:
        print("Invalid choice.")