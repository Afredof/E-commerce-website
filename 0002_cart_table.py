# Generated by Django 4.2.1 on 2024-04-11 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Userapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.PositiveBigIntegerField(default=1)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Userapp.reg_table')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Userapp.item_table')),
            ],
        ),
    ]
