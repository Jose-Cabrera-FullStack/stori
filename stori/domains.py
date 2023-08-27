import datetime


class StoriDomain:

    @staticmethod
    def total_balance(transactions: list, decimals: int = 2) -> float:
        """ Calculate the total balance. """
        result = sum(transactions)
        return round(result, decimals)

    @staticmethod
    def average_by_month(transactions: dict) -> dict:
        """
        Calculate the average amount by month.
        :param
        transactions: dict with key as date and value as credit/debit transaction.
        :return
        average_amount_by_month: dict with key as month and value as average amount.
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
        average_amount_by_month = {}
        decimals = 2

        for date, value in transactions.items():
            format_date = StoriDomain._format_date(date)
            if format_date in average_amount_by_month:
                average_amount_by_month[format_date] += value
                repeated_date[format_date] += 1
            else:
                average_amount_by_month[format_date] = value
                repeated_date[format_date] = 1

        for date, value in average_amount_by_month.items():
            if repeated_date[date] > 1:
                average_amount_by_month[date] = round(
                    value / repeated_date[date], decimals)

        return average_amount_by_month

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
