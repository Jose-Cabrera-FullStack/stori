from django.test import TestCase

from stori.domains import StoriDomain


class TestStoriDomain(TestCase):

    def setUp(self):
        self.transactions = {
            "7/15": 60.5,
            "7/16": -20.46,
            "8/15": 100.0,
            "8/16": -50.0
        }

    def test_total_balance(self):
        total_bal = StoriDomain.total_balance(list(self.transactions.values()))
        self.assertEqual(total_bal, 90.04)

    def test_average_by_month(self):
        average_by_month = StoriDomain.average_by_month(self.transactions)
        expected_result = {
            "July": 20.02,
            "August": 25.0
        }
        self.assertDictEqual(average_by_month, expected_result)

    def test_transactions_by_month(self):
        transactions_by_month = StoriDomain.transactions_by_month(
            self.transactions)
        expected_result = {
            "July": 2,
            "August": 2
        }
        self.assertDictEqual(transactions_by_month, expected_result)

    def test_format_date(self):
        formatted_date = StoriDomain._format_date("7/15")
        self.assertEqual(formatted_date, "July")
