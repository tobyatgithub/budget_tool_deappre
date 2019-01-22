# Generated by Django 2.1.5 on 2019-01-22 02:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='date_modified',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='date_uploaded',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]