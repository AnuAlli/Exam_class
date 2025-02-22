# expense_tracker.py

import uuid
from datetime import datetime, timezone

class Expense:
    def __init__(self, title: str, amount: float):
        """
        Initialize an expense with a title and amount.
        Automatically generates UUID and timestamps.
        """
        self.id = str(uuid.uuid4())
        self.title = title
        self.amount = float(amount)
        self.created_at = datetime.now(timezone.utc)
        self.updated_at = self.created_at

    def update(self, title: str = None, amount: float = None):
        """
        Update the expense title and/or amount.
        Automatically updates the updated_at timestamp.
        """
        if title is not None:
            self.title = title
        if amount is not None:
            self.amount = float(amount)
        self.updated_at = datetime.now(timezone.utc)

    def to_dict(self):
        """
        Convert the expense object to a dictionary.
        """
        return {
            'id': self.id,
            'title': self.title,
            'amount': self.amount,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

class ExpenseDB:
    def __init__(self):
        """
        Initialize an empty expense database.
        """
        self.expenses = []

    def add_expense(self, expense: Expense):
        """
        Add an expense to the database.
        """
        self.expenses.append(expense)

    def remove_expense(self, expense_id: str):
        """
        Remove an expense from the database by ID.
        """
        self.expenses = [exp for exp in self.expenses if exp.id != expense_id]

    def get_expense_by_id(self, expense_id: str) -> Expense:
        """
        Get an expense by ID.
        Returns None if not found.
        """
        for expense in self.expenses:
            if expense.id == expense_id:
                return expense
        return None

    def get_expenses_by_title(self, title: str) -> list:
        """
        Get all expenses with matching title.
        Returns empty list if none found.
        """
        return [exp for exp in self.expenses if exp.title == title]

    def to_dict(self) -> list:
        """
        Convert all expenses to a list of dictionaries.
        """
        return [expense.to_dict() for expense in self.expenses]