# Generated by Django 4.1.6 on 2023-06-03 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0049_alter_account_special_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journalentry',
            name='transaction',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='journal_entries', to='api.transaction'),
        ),
    ]