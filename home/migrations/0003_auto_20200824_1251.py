# Generated by Django 3.1 on 2020-08-24 04:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='status',
            name='content',
        ),
        migrations.RemoveField(
            model_name='status',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='status',
            name='title',
        ),
        migrations.RemoveField(
            model_name='status',
            name='update_time',
        ),
    ]
