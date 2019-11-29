# Generated by Django 2.2.4 on 2019-11-25 14:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0011_auto_20191125_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='full_address',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orders',
            name='postcode',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orders',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
