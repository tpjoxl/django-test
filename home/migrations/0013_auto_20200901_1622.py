# Generated by Django 3.1 on 2020-09-01 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20200901_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statu',
            name='content',
            field=models.TextField(blank=True, max_length=70),
        ),
    ]
