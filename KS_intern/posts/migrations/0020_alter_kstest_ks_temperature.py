# Generated by Django 4.0.1 on 2022-01-23 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0019_kstest_ks_temperature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kstest',
            name='ks_temperature',
            field=models.IntegerField(default='0'),
        ),
    ]
