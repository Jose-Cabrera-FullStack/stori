from stori.adapters import StoriAdapter
from stori.domains import StoriDomain


class StoriService:

    @staticmethod
    def send_summary_balance() -> dict:
        """ Example of Service: Get data from database """

        transactions_list = StoriAdapter.extract_data_from_csv(
            file_path='stori/temp/stori_transaction_data.csv'
        )

        total_balance = StoriDomain.total_balance(transactions_list)

        average_credit = StoriDomain.average_credit_by_month(
            transactions_list
        )

        average_debit = StoriDomain.average_debit_by_month(
            transactions_list
        )

        transactions = StoriDomain.transaction_number_by_month(
            transactions_list
        )

        # TODO: Send data to email

        # TODO: Send data to database

        return
