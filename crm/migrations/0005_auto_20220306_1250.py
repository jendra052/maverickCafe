# Generated by Django 3.2.3 on 2022-03-06 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0004_merge_0003_auto_20220303_1327_customer_account'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='account',
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=50),
        ),
    ]
