# main

from expenses import add_expense, view_expenses, get_total_expenses
from utils import is_valid_amount

def main():
    print("Welcome to the Expense Tracker!")
    
    while True:
        print("\nOptions:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Get Total Expenses")
        print("4. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            category = input("Enter category (e.g., food, transport): ")
            amount_str = input("Enter amount: ")

            if is_valid_amount(amount_str):
                amount = float(amount_str)
                add_expense(category, amount)
                print(f"${amount:.2f} added to {category} category.")
            else:
                print("Invalid amount. Please enter a number.")

        elif choice == '2':
            print("\nYour Expenses:")
            view_expenses()

        elif choice == '3':
            total = get_total_expenses()
            print(f"\nTotal Expenses: ${total:.2f}")

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
