import datetime


class StoriDomain:

    @staticmethod
    def total_balance(transactions: list) -> float:
        """ Calculate the total balance. """
        return sum(transactions)

    @staticmethod
    def average_by_month(transactions: dict) -> dict:
        """
        transactions: dict with key as date and value as credit/debit transaction.
        """

        try:
            transactions = {
                datetime.datetime.strptime(key, '%m/%d').strftime('%m/%d'): value
                for key, value in transactions.items()
            }
        except ValueError:
            raise ValueError(
                'Invalid date format. transaction date must be in format: %m/%d')
        except Exception as error:
            raise Exception(error)

        repeated_date = {}
        average_credit_by_month = {}

        for date, value in transactions.items():
            format_date = StoriDomain._format_date(date)
            if format_date in average_credit_by_month:
                average_credit_by_month[format_date] += value
                repeated_date[format_date] += 1
            else:
                average_credit_by_month[format_date] = value
                repeated_date[format_date] = 1

        for date, value in average_credit_by_month.items():
            if repeated_date[date] > 1:
                average_credit_by_month[date] = value / repeated_date[date]

        return average_credit_by_month

    @staticmethod
    def transactions_by_month(transactions: dict) -> dict:
        """ Group transactions by month and year. """

        transactions_by_month = {}

        for key, _ in transactions.items():
            format_date = StoriDomain._format_date(key)
            if format_date in transactions_by_month:
                transactions_by_month[format_date] += 1
            else:
                transactions_by_month[format_date] = 1

        return transactions_by_month

    @staticmethod
    def _format_date(date: str, from_format_date: str = "%m/%d", to_format_date: str = "%B") -> dict:
        return datetime.datetime.strptime(date, from_format_date).strftime(to_format_date)
