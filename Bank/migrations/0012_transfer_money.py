# Generated by Django 3.1.7 on 2021-04-12 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bank', '0011_auto_20210412_2151'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transfer_money',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SenderName', models.CharField(blank=True, max_length=122, null=True)),
                ('SenderAccountNo', models.CharField(blank=True, max_length=7, null=True)),
                ('RecieverName', models.CharField(blank=True, max_length=122, null=True)),
                ('RecieverAccountNo', models.CharField(blank=True, max_length=7, null=True)),
                ('Amount', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]