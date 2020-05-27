from django.db import models

# Create your models here.
class Account(models.Model):
    account_Num = models.CharField(max_length=10, default="", blank=True, null=False, unique=True)
    name_first = models.CharField(max_length=100, default="", blank=True, null=False)
    name_last = models.CharField(max_length=100, default="", blank=True, null=False)
    balance = models.DecimalField(max_digits=100000, decimal_places=2, default="", blank=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return self.account_Num

TRANSACTION_TYPES = {
    ('debit', 'Debit'),
    ('credit', 'Credit'),
    ('cash', 'Cash'),
}



class Transaction(models.Model):
    date = models.DateTimeField(auto_now_add=True, blank=True)
    type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    description = models.CharField(max_length=100, default="", blank=True, null=False)
    amount = models.DecimalField(max_digits=100000, decimal_places=2, default="", blank=True, null=False)
    account = models.ForeignKey('Account', related_name='transaction', on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return str(self.pk)