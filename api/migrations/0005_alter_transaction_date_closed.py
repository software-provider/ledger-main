# Generated by Django 4.1.6 on 2023-02-10 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_account_number_remove_transaction_party_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date_closed',
            field=models.DateField(blank=True, null=True),
        ),
    ]