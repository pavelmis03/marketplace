# Generated by Django 2.2.10 on 2020-06-01 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0021_auto_20200602_0034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='market',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogue.Market'),
        ),
    ]
