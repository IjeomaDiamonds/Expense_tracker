class ExpenseDB:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def remove_expense(self, expense_id: str):
        self.expenses = [e for e in self.expenses if e.id != expense_id]

    def get_expense_by_id(self, expense_id: str):
        for expense in self.expenses:
            if expense.id == expense_id:
                return expense
        return None

    def get_expense_by_title(self, title: str):
        return [e for e in self.expenses if e.title == title]

    def to_dict(self):
        return [expense.to_dict() for expense in self.expenses]