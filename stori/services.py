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
            df_transactions['Transaction']).to_list()

        average_credit = StoriDomain.average_credit_by_month(
            transactions_list
        )

        average_debit = StoriDomain.average_debit_by_month(
            transactions_list
        )

        transactions_by_month = StoriDomain.transaction_number_by_month(
            transactions_list
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
