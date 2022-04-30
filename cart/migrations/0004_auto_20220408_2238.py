# Generated by Django 3.2.12 on 2022-04-08 22:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_auto_20220323_0156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='id',
        ),
        migrations.AddField(
            model_name='cart',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cart',
            name='user_id',
            field=models.CharField(default='none', max_length=200),
        ),
        migrations.AlterField(
            model_name='cart',
            name='cart_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.cart'),
        ),
    ]
