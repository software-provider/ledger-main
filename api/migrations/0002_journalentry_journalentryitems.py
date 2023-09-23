# Generated by Django 4.1.6 on 2023-02-09 00:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JournalEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('description', models.CharField(max_length=200)),
                ('journal_entry', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.transaction')),
            ],
        ),
        migrations.CreateModel(
            name='JournalEntryItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('D', 'Debit'), ('C', 'Credit')], max_length=1)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.account')),
                ('journel_entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.journalentry')),
            ],
        ),
    ]
