import datetime
import pandas as pd

from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

from setup import settings
from stori.models import Transaction
from stori.adapters import StoriAdapter
from stori.domains import StoriDomain


class StoriService:

    @staticmethod
    def send_summary_balance() -> dict:
        """ Send summary balance to email and save data to database """

        df_transactions = StoriAdapter.extract_data_from_csv()

        summary_balance = StoriService._build_summary_balance(df_transactions)

        StoriService._send_email(summary_balance)

        StoriService._save_transactions(df_transactions.values.tolist())

        return summary_balance

    @staticmethod
    def _build_summary_balance(df_transactions: pd.DataFrame) -> dict:
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

        month_data = []
        for month, transaction_count in transactions_by_month.items():
            month_data.append((
                month,
                transaction_count,
                average_credit[month],
                average_debit[month]
            ))

        summary_balance = {
            'total_balance': total_balance,
            'month_data': month_data,
        }

        return summary_balance

    @staticmethod
    def _send_email(summary_balance: dict) -> None:
        """ Send data to email """

        html_content = render_to_string(
            "summary_balance.html",
            {
                'total_balance': summary_balance['total_balance'],
                'month_data': summary_balance['month_data'],
            })

        text_context = strip_tags(html_content)

        email = EmailMultiAlternatives(
            subject='Stori - Summary Balance',
            body=text_context,
            from_email=settings.EMAIL_HOST_USER,
            to=[settings.EMAIL_FROM],
        )
        email.attach_alternative(html_content, "text/html")
        email.send()

    @staticmethod
    def _save_transactions(transactions: list) -> None:
        """ Save data to database """

        bulk_transactions = []

        for transaction in transactions:
            date = transaction[1]
            date = datetime.datetime.strptime(date, "%m/%d")
            amount = transaction[2]
            transaction_type = "credit" if amount > 0 else "debit"
            transaction = Transaction(
                date=date,
                amount= float(amount),
                transaction_type=transaction_type
            )
            bulk_transactions.append(transaction)

        Transaction.objects.bulk_create(bulk_transactions)
