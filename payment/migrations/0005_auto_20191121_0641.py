# Generated by Django 2.2.4 on 2019-11-21 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_auto_20191121_0632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='urgency',
            name='name',
        ),
        migrations.AddField(
            model_name='urgency',
            name='urgency_tag',
            field=models.CharField(choices=[('Urgent', 'Urgent'), ('Important', 'Important'), ('Flexible', 'Flexible')], default='Urgent', max_length=50),
        ),
    ]