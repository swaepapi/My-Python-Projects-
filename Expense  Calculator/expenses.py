# expenses

# Dictionary to store expenses by category
expenses = {}

def add_expense(category, amount):
    """Adds an expense to the specified category."""
    if category in expenses:
        expenses[category] += amount
    else:
        expenses[category] = amount

def view_expenses():
    """Displays all expenses by category."""
    for category, amount in expenses.items():
        print(f"{category}: ${amount:.2f}")

def get_total_expenses():
    """Returns the total expenses."""
    total = sum(expenses.values())
    return total
