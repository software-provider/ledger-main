# Generated by Django 4.1.6 on 2023-02-23 01:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_account_default_transaction_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='default_transaction_type',
        ),
    ]