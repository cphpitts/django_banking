# Generated by Django 3.0.6 on 2020-05-27 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200527_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='type',
            field=models.CharField(choices=[('cash', 'Cash'), ('credit', 'Credit'), ('debit', 'Debit')], max_length=10),
        ),
    ]
