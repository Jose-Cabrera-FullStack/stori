from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail
from django.conf import settings

from stori.models import Transaction
from stori.adapters import StoriAdapter
from stori.domains import StoriDomain


class StoriService:

    @staticmethod
    def send_summary_balance() -> dict:
        """ Send summary balance to email and save data to database """

        df_transactions = StoriAdapter.extract_data_from_csv()

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

        summary_balance = {
            'total_balance': total_balance,
            'average_credit_by_month': average_credit,
            'average_debit_by_month': average_debit,
            'transactions_by_month': transactions_by_month,
        }

        # TODO: Send data to email
        StoriService._send_email(summary_balance)

        # TODO: Send data to database
        # StoriService._save_transactions(transactions_list)

        return summary_balance

    @staticmethod
    def _send_email(summary_balance: dict) -> None:
        """ Send data to email """

        html_content = render_to_string(
            "summary_balance.html",
            {'total_balance': summary_balance['total_balance'],
             'transactions_by_month': summary_balance['transactions_by_month'],
             'average_credit_by_month': summary_balance['average_credit_by_month'],
             'average_debit_by_month': summary_balance['average_debit_by_month'],
             })

        text_context = strip_tags(html_content)

        email = EmailMultiAlternatives(
            subject='Stori - Summary Balance',
            body=text_context,
            # from_email=settings.EMAIL_HOST_USER,
            from_email="murdoc.jose.6@gmail.com",
            to=['murdoc.jose.6@gmail.com'],
        )
        email.attach_alternative(html_content, "text/html")
        email.send()

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
