# Generated by Django 3.1.5 on 2021-03-28 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_auto_20210321_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_ordered',
            field=models.DateTimeField(max_length=100, null=True),
        ),
    ]
