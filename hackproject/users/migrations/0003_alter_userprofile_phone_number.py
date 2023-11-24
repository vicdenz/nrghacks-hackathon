# Generated by Django 4.2.4 on 2023-10-09 02:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_userprofile_delete_profileuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone_number',
            field=models.CharField(blank=True, help_text='Phone number in the format (123)-456-7890.', max_length=15, validators=[django.core.validators.RegexValidator(code='invalid_phone_number', message='Enter a valid phone number in the format (123)-456-7890.', regex='^\\(\\d{3}\\)-\\d{3}-\\d{4}$')], verbose_name='Phone number'),
        ),
    ]