# Generated by Django 3.1.3 on 2020-11-22 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viberapi', '0002_auto_20201119_2333'),
    ]

    operations = [
        migrations.AddField(
            model_name='viberuser',
            name='bitrix_id',
            field=models.IntegerField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='viberuser',
            name='viber_id',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
