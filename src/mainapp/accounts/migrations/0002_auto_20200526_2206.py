# Generated by Django 3.0.6 on 2020-05-27 05:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_Num',
            field=models.CharField(blank=True, default='', max_length=10, unique=True),
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(blank=True, default='', max_length=100)),
                ('type', models.CharField(choices=[('debit', 'Debit'), ('cash', 'Cash'), ('credit', 'Credit')], max_length=10)),
                ('description', models.CharField(blank=True, default='', max_length=100)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, default='', max_digits=100000)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.Account', to_field='account_Num')),
            ],
        ),
    ]