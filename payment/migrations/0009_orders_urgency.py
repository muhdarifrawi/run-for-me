# Generated by Django 2.2.4 on 2019-11-21 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0008_auto_20191121_1302'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='urgency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='payment.Urgency'),
        ),
    ]
