# Generated by Django 4.2.1 on 2024-04-12 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Userapp', '0007_alter_pay_table_qty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pay_table',
            name='ex',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='pay_table',
            name='fn',
            field=models.CharField(max_length=25),
        ),
    ]
