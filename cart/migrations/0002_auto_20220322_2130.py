# Generated by Django 3.2.12 on 2022-03-22 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='cart_id',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='cart',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='product',
            field=models.IntegerField(),
        ),
    ]
