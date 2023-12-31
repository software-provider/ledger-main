# Generated by Django 4.1.6 on 2023-02-13 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_transaction_suggested_type_transaction_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='autotag',
            name='transaction_type',
            field=models.CharField(blank=True, choices=[('income', 'Income'), ('purchase', 'Purchase'), ('payment', 'Payment'), ('transfer', 'Transfer')], max_length=8),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='suggested_type',
            field=models.CharField(blank=True, choices=[('income', 'Income'), ('purchase', 'Purchase'), ('payment', 'Payment'), ('transfer', 'Transfer')], max_length=8),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='type',
            field=models.CharField(blank=True, choices=[('income', 'Income'), ('purchase', 'Purchase'), ('payment', 'Payment'), ('transfer', 'Transfer')], max_length=8),
        ),
    ]
