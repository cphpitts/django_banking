# Generated by Django 3.0.6 on 2020-05-27 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20200527_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='type',
            field=models.CharField(choices=[('debit', 'Debit'), ('credit', 'Credit'), ('cash', 'Cash')], max_length=10),
        ),
    ]