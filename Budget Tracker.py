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

    def total_expenses(self):
        """Calculate the total amount of expenses."""
        return sum(expense['amount'] for expense in self.expenses)


    def budget_summary(self):
        """Display a summary of the budget."""
        total_expense = self.total_expenses()
        balance = self.income - total_expense


        print("\n--- Budget Summary ---")
        print(f"Total Income: ${self.income:.2f}")
        print(f"Total Expenses: ${total_expense:.2f}")
        print(f"Balance: ${balance:.2f}")


        if balance < 0:
            print("Warning: You are over budget!")
        elif balance == 0:
            print("You are breaking even.")
        else:
            print("Great! You are under budget.")


    d