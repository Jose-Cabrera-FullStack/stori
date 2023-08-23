from django.db import models


class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('credit', 'Credit'),
        ('debit', 'Debit'),
    )

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    transaction_type = models.CharField(
        max_length=10,
        choices=TRANSACTION_TYPES
    )

    def __str__(self):
        return f"{self.transaction_type} - {self.amount} ({self.date})"
