# Generated by Django 4.2.7 on 2023-12-04 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0033_fee_fee_id_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='name',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]
