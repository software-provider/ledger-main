# Generated by Django 4.1.6 on 2023-02-13 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_remove_autotag_accounts_autotag_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='suggested_account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='suggested_account', to='api.account'),
        ),
    ]
