from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from stori.models import Transaction
from stori.adapters import StoriAdapter
from stori.domains import StoriDomain


class StoriService:

    @staticmethod
    def send_summary_balance(request: dict) -> dict:
        """ Send summary balance to email and save data to database """

        df_transactions = StoriAdapter.extract_data_from_csv(
            file_path='./temp/stori_transaction_data.csv'
        )

        total_balance = StoriDomain.total_balance(
            df_transactions['Transaction'].to_list())

        date_transaction = df_transactions.set_index(
            'Date')['Transaction'].to_dict()

        # TODO: filter by date_transaction positive transactions (credit)
        credit_date_transaction = df_transactions.set_index(
            'Date')['Transaction'].to_dict()

        # TODO: filter by date_transaction negative transactions (debit)
        debit_date_transaction = df_transactions.set_index(
            'Date')['Transaction'].to_dict()

        average_credit = StoriDomain.average_by_month(
            credit_date_transaction
        )

        average_debit = StoriDomain.average_by_month(
            debit_date_transaction
        )

        transactions_by_month = StoriDomain.transactions_by_month(
            date_transaction
        )

        context = {
            'total_balance': total_balance,
            'average_credit': average_credit,
            'average_debit': average_debit,
            'transactions_by_month': transactions_by_month,
        }

        # TODO: Send data to email
        render(request, 'transactions/summary.html', context)

        # TODO: Send data to database
        StoriService._save_transactions(transactions_list)

        return context

    @staticmethod
    def _save_transactions(transactions_list: list) -> None:
        """ Save data to database """

        bulk_transactions = []

        for transaction in transactions_list:
            transaction = Transaction(
                date=transaction['date'],
                amount=transaction['amount'],
                description=transaction['description'],
            )
            bulk_transactions.append(transaction)

        Transaction.objects.bulk_create(bulk_transactions)
