from Expense import Expense
from Expense_db import ExpenseDB

# Create an ExpenseDB instance
db = ExpenseDB()

# Add expenses
expense1 = Expense("Groceries", 50.0)
expense2 = Expense("Utilities", 100.0)
db.add_expense(expense1)
db.add_expense(expense2)

# Print all expenses
print("All Expenses:")
print(db.to_dict())

# Update an expense
expense1.update(title="Supermarket", amount=55.0)
print("\nUpdated Expense:")
print(expense1.to_dict())

# Remove an expense
db.remove_expense(expense2.id)
print("\nExpenses after removal:")
print(db.to_dict())

# Get expense by ID
print("\nGet Expense by ID:")
print(db.get_expense_by_id(expense1.id).to_dict())

# Get expenses by title
print("\nGet Expenses by Title:")
print(db.get_expense_by_title("Supermarket"))