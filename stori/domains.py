import datetime


class StoriDomain:

    @staticmethod
    def total_balance(transactions: list) -> float:
        """ Calculate the total balance. """
        return sum(transactions)

    @staticmethod
    def average_by_month(transactions: dict) -> dict:
        """ Group average credit transactions by month and year. """

        # TODO: validate if the date is valid or format to valid date
        # transactions

        repeated_date = {}
        average_credit_by_month = {}

        for key, value in transactions.items():
            if key in average_credit_by_month:
                average_credit_by_month[key] += value
                repeated_date[key] += 1
            else:
                average_credit_by_month[key] = value
                repeated_date[key] = 1

        for key, value in average_credit_by_month.items():
            if repeated_date[key] > 1:
                average_credit_by_month[key] = value / repeated_date[key]

        return average_credit_by_month

    @staticmethod
    def transactions_by_month(transactions: dict) -> dict:
        """ Group transactions by month and year. """

        transactions_by_month = {}

        for key, _ in transactions.items():
            if key in transactions_by_month:
                transactions_by_month[key] += 1
            else:
                transactions_by_month[key] = 1

        return transactions_by_month
