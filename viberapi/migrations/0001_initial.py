# Generated by Django 3.1.3 on 2020-11-19 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ViberUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('viber_id', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=200)),
                ('language', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('subscribed', models.BooleanField()),
            ],
        ),
    ]