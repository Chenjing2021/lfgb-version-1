# Generated by Django 3.1.5 on 2021-03-17 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_order_transaction_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='categories',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
