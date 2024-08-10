class BudgetTracker:
    def __init__(self):
        """Initialize the budget tracker with empty income and expenses."""
        self.income = 0.0  # Total income
        self.expenses = []  # List to store expenses

    def add_income(self, amount):
        """
        Add income to the budget.

        Args:
            amount (float): The income amount to add.
        """
        self.income += amount
        print(f"Income added: ${amount:.2f}")

    def add_expense(self, description, amount):
        """
        Add an expense to the budget.

        Args:
            description (str): A description of the expense.
            amount (float): The expense amount to add.
        """
        self.expenses.append({"description": description, "amount": amount})
        print(f"Expense added: {description} - ${amount:.2f}")

    