# Generated by Django 3.0.6 on 2020-05-27 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20200527_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='type',
            field=models.CharField(choices=[('credit', 'Credit'), ('cash', 'Cash'), ('debit', 'Debit')], max_length=10),
        ),
    ]