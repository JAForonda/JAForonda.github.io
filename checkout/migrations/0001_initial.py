# Generated by Django 3.2.12 on 2022-03-25 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('payment_id', models.IntegerField()),
                ('user_id', models.CharField(max_length=200)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('phone', models.IntegerField()),
                ('email', models.CharField(max_length=300)),
                ('address', models.CharField(max_length=400)),
                ('address2', models.CharField(max_length=400)),
                ('country', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('notes', models.TextField()),
                ('total', models.FloatField()),
                ('tax', models.FloatField()),
                ('status', models.CharField(max_length=30)),
                ('is_ordered', models.BooleanField(default=False)),
                ('ip', models.CharField(max_length=20)),
                ('created_date', models.DateTimeField()),
                ('updatd_date', models.DateTimeField()),
            ],
        ),
    ]
