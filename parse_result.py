from transaction import Transaction


class ParseResult:
    def __init__(self, initial_balance, end_balance, expenses, incomes):
        self.initial_balance = initial_balance
        self.end_balance = end_balance
        self.expenses = expenses
        self.incomes = incomes
