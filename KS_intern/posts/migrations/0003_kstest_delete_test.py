# Generated by Django 4.0.1 on 2022-01-20 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_test_remove_post_location_delete_location_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='kstest',
            fields=[
                ('ks_ID', models.AutoField(primary_key=True, serialize=False)),
                ('ks_Name', models.CharField(max_length=20)),
                ('ks_time', models.DateTimeField(max_length=6)),
            ],
        ),
        migrations.DeleteModel(
            name='Test',
        ),
    ]
