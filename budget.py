class Category:
    def __init__(self, category):
        # Initialize the Category object with a name and an empty ledger
        self.category = category
        self.ledger = []

    def deposit(self, amount, description=""):
        # Record a deposit in the ledger
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            # Only subtract the amount once
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        # Calculate the current balance based on the ledger
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, budget_category):
        # Transfer funds between two budget categories
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {budget_category.category}")
            budget_category.deposit(amount, f"Transfer from {self.category}")
            return True
        return False

    def check_funds(self, amount):
        # Check if there are enough funds for a withdrawal or transfer
        return amount <= self.get_balance()

    def __str__(self):
        # Format the object as a string for printing
        title = f"{self.category:*^30}\n"
        items = ""
        for item in self.ledger:
            items += f"{item['description'][:23]:23}{item['amount']:>7.2f}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    # Create a bar chart showing the percentage spent by category
    chart = "Percentage spent by category\n"
    spendings = [(c.category, sum(item['amount'] for item in c.ledger if item['amount'] < 0)) for c in categories]
    total_spent = sum(spend for _, spend in spendings)

    if total_spent == 0:
        # Avoid division by zero
        percentages = [0] * len(categories)
    else:
        percentages = [int(spent / total_spent * 100) for _, spent in spendings]

    for i in range(100, -1, -10):
        chart += f"{i:3}| "
        for percentage in percentages:
            bar = "o" if percentage >= i else " "
            chart += f"{bar:2}  "
        chart += "\n"

    chart += "    ----------\n     "
    max_length = max(len(c.category) for c in categories)
    for i in range(max_length):
        for category in categories:
            if i < len(category.category):
                chart += f"{category.category[i]}  "
            else:
                chart += "   "
        if i < max_length - 1:
            chart += "\n     "

    return chart


