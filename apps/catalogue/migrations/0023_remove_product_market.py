# Generated by Django 2.2.10 on 2020-06-01 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0022_auto_20200602_0035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='market',
        ),
    ]
