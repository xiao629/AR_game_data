# Generated by Django 4.0.1 on 2022-01-23 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_alter_kstest_ks_temperature'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kstest',
            name='ks_temperature',
        ),
    ]
