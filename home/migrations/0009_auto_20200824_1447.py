# Generated by Django 3.1 on 2020-08-24 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20200824_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='statu',
            name='QOS',
            field=models.CharField(default=0, max_length=2),
        ),
        migrations.AddField(
            model_name='statu',
            name='datatype',
            field=models.TextField(blank=True),
        ),
    ]
