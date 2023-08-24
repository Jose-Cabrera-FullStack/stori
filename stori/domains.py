class StoriDomain:

    @staticmethod
    def total_balance(transactions: list) -> float:
        """ Calculate the total balance. """
        return sum([transaction['amount'] for transaction in transactions])

    @staticmethod
    def transaction_number_by_month(transactions: list) -> dict:
        """ Calculate the number of transactions by month. """
        months = [transaction['Date'].month for transaction in transactions]
        return {month: months.count(month) for month in months}

    @staticmethod
    def average_credit_by_month(transactions: list) -> float:
        """ Calculate the average of credit by month. """
        credits = [transaction['amount']
                   for transaction in transactions if transaction['amount'] > 0]
        return sum(credits) / len(credits)

    @staticmethod
    def average_debit_by_month(transactions: list) -> float:
        """ Calculate the average of debit by month. """
        debits = [transaction['amount']
                  for transaction in transactions if transaction['amount'] < 0]
        return sum(debits) / len(debits)
