# Generated by Django 3.1.7 on 2021-04-18 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bank', '0014_bank_statement_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer_money',
            name='Date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
